from casadi import *

import config
from local_sim.kinematics.cartesian import CartesianKinematics


class LocalPlanner:
    def __init__(self, dT, T):
        self.optimizer = Opti()
        self.dT = dT
        self.T = T
        self.N = int(T / dT)

    def find_path(self, current_state, end_state, total_dist, obstacles, dynamic_obstacles):
        # Decision variables
        state = self.optimizer.variable(4, self.N)
        u = self.optimizer.variable(2, self.N - 1)

        # Set up cost function
        cost = 0

        for i in range(self.N):
            cost += (state[0, i] - end_state[0]) ** 2
            cost += (state[1, i] - end_state[1]) ** 2

            dist = (end_state[1] - current_state[1]) ** 2 + (end_state[0] - current_state[0]) ** 2
            dist_ratio = ((total_dist - dist) / total_dist) ** 4

            cost += dist_ratio * state[2, i] ** 2
            cost += dist_ratio * state[3, i] ** 2

        # for i in range(self.N - 1):
        #     cost += u[0, i] ** 2
        #     cost += u[1, i] ** 2

        for obstacle in dynamic_obstacles:
            cost += 1 / ((state[0, 0] - obstacle.x) ** 2 + (state[1, 0] - obstacle.y) ** 2)

        self.optimizer.minimize(cost)

        # Set up constraints
        for constraint in CartesianKinematics.get_constraints(state, u, self.dT, self.N):
            self.optimizer.subject_to(constraint)

        for obstacle in obstacles:
            for i in range(self.N):
                self.optimizer.subject_to(
                    (state[0, i] - obstacle.x) ** 2 + (state[1, i] - obstacle.y) ** 2 >= (
                            obstacle.radius ** 2 + config.padding ** 2))

        for i in range(4):
            self.optimizer.subject_to(state[i, 0] == current_state[i])

        # Apply velocity bounds
        for i in range(self.N):
            self.optimizer.subject_to(self.optimizer.bounded(-50, state[2, i], 50))
            self.optimizer.subject_to(self.optimizer.bounded(-50, state[3, i], 50))

        # Apply acceleration bounds
        for i in range(self.N - 1):
            self.optimizer.subject_to(self.optimizer.bounded(-30, u[0, i], 10))
            self.optimizer.subject_to(self.optimizer.bounded(-30, u[1, i], 10))

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
