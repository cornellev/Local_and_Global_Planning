import math

from casadi import *
from matplotlib import pyplot as plt

from local_sim.kinematics.cartesian import CartesianKinematics
from local_sim.obstacle import Obstacle


class LocalPlanner:
    def __init__(self, dT, T):
        self.optimizer = Opti()
        self.dT = dT
        self.T = T
        self.N = int(T / dT)

        self.obstacle_padding = .5

    def find_path(self, current_state, end_state, next_waypoint, total_dist, obstacles):
        # Decision variables
        state = self.optimizer.variable(4, self.N)
        u = self.optimizer.variable(2, self.N - 1)

        # Set up cost function
        cost = 0

        for i in range(self.N):
            cost += (state[0, i] - end_state[0]) ** 2
            cost += (state[1, i] - end_state[1]) ** 2

            # Angle the velocity towards the next waypoint or set vel to zero if end node
            dist = (end_state[1] - current_state[1]) ** 2 + (end_state[0] - current_state[0]) ** 2
            dist_ratio = ((total_dist - dist) / total_dist) ** 8

            print(dist)
            print(total_dist)
            print(dist_ratio)

            if next_waypoint is None:
                cost += dist_ratio * state[2, i] ** 2
                cost += dist_ratio * state[3, i] ** 2
            else:
                angle = math.atan2(next_waypoint[1] - end_state[1], next_waypoint[0] - end_state[0])
                x = 2.5 * cos(angle)
                y = 2.5 * sin(angle)

                cost += 1 * dist_ratio * (state[2, i] - x) ** 2
                cost += 1 * dist_ratio * (state[3, i] - y) ** 2

        for i in range(self.N - 1):
            cost += u[0, i] ** 2
            cost += u[1, i] ** 2

        self.optimizer.minimize(cost)

        # Set up constraints
        for constraint in CartesianKinematics.get_constraints(state, u, self.dT, self.N):
            self.optimizer.subject_to(constraint)

        for obstacle in obstacles:
            for i in range(self.N):
                x = state[0, i]
                y = state[1, i]
                dist_from_center = (x - obstacle.x) ** 2 + (y - obstacle.y) ** 2

                self.optimizer.subject_to(
                    dist_from_center >= (obstacle.radius ** 2 + self.obstacle_padding ** 2))

        for i in range(4):
            self.optimizer.subject_to(state[i, 0] == current_state[i])

        # Apply velocity bounds
        for i in range(self.N):
            self.optimizer.subject_to(self.optimizer.bounded(-50, state[2, i], 50))
            self.optimizer.subject_to(self.optimizer.bounded(-50, state[3, i], 50))

        # Apply acceleration bounds
        for i in range(self.N - 1):
            self.optimizer.subject_to(self.optimizer.bounded(-10, u[0, i], 10))
            self.optimizer.subject_to(self.optimizer.bounded(-10, u[1, i], 10))

        # Calculate solution
        opts = {'ipopt.print_level': 0, 'print_time': 0, 'ipopt.sb': 'yes'}
        self.optimizer.solver('ipopt', opts)

        solution = self.optimizer.solve()

        return solution, state, u

    @staticmethod
    def get_path_coords(solution, state):
        x_s, y_s, vx_s, vy_s = solution.value(state)

        path = []

        for i in range(len(x_s)):
            path.append([x_s[i], y_s[i], vx_s[i], vy_s[i]])

        return path


# start_state = [0, 0, 0, 0]
# end_state = [4, 4, 0, 0]
#
# obstacles = [
#     Obstacle(1.5, 1.5, 1),
#     Obstacle(2.5, 2.5, .3),
#     Obstacle(3, 2, .5),
#     Obstacle(2.5, 4, .3)
# ]

# planner = LocalPlanner(.05, 10)
# solution, state, u = planner.find_path(start_state, end_state, obstacles)
#
# x_s, y_s, vx_s, vy_s = solution.value(state)
# ax_s, ay_s = solution.value(u)
#
# # Plot trajectory
# plt.figure(figsize=(10, 6))
# plt.subplot(2, 1, 1)
# plt.plot(x_s, y_s, label='Trajectory')
# plt.scatter(end_state[0], end_state[1], color='red', label='Obstacle')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Trajectory')
# plt.legend()
#
# # Plot velocity profile
# plt.subplot(2, 1, 2)
# plt.plot(vx_s, label='X Velocity')
# plt.plot(vy_s, label='Y Velocity')
# plt.xlabel('Time Step')
# plt.ylabel('Velocity')
# plt.title('Velocity Profile')
# plt.legend()
#
# plt.tight_layout()
# plt.show()
#
# # Plot trajectory on a coordinate plane with obstacle
# plt.figure(figsize=(8, 6))
# plt.scatter(x_s, y_s, label='Trajectory', color='blue')
# plt.scatter(end_state[0], end_state[1], label='Obstacle', color='red')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Trajectory with Obstacles')
# plt.legend()
# plt.grid(True)
# plt.axis('equal')
#
# for obstacle in obstacles:
#     obstacle.plot()
#
# plt.show()
