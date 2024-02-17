from casadi import *
import matplotlib.pyplot as plt

import math 

class Constraint:
    def __init__(self):
        pass

    def get_constraints(self, x, u, dt, N):
        # put formal
        raise NotImplementedError()

class RectangleConstraint(Constraint):
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def get_constraints(self, x, u, dt, N):
        constraints = []
        # for i in range(N):
        #     constraints.append([x[0,i] >= self.x + self.w/2, x[0,i] <= self.x - self.w/2])
        #     constraints.append([x[1,i] >= self.y + self.h/2, x[1,i] <= self.y - self.h/2])
        return constraints

class KinematicConstraint(Constraint):
    def __init__(self):
        super().__init__()

    def get_constraints(self, x, u, dt, N):
        constraints = []
        
        for i in range(N-1):
            # update accel_x
            # vx_i+1 = vx_i + ax_i * dt
            constraints.append(x[2, i+1] == x[2, i] + u[0, i] * dt)
            
            # update accel_Y
            # vy_i+1 = vx_i + ay_i * dt
            constraints.append(x[3, i+1] == x[3, i] + u[1, i] * dt)

            # update vel_x
            # x_i+1 = x_i + vx_i * dt
            constraints.append(x[0, i+1] == x[0, i] + x[2, i] * dt)

            # update vel_y
            # y_i+1 = y_i + vy_i * dt
            constraints.append(x[1, i+1] == x[1, i] + x[3, i] * dt)

        return constraints


# navigate a model that that can accelerate in both axes around obstacles optimally
opti = Opti()

T = 10.0 # How far ahead to look for from the current state in total
dt = 0.02 # How long to look ahead per iter
num_time_steps = int(T/dt) # (N) Number of time steps to look into the future for

# target [x, y, x', y']
target_state = [4, 4, 0, 0] # (r) Reference state


# Decision variables (symbolic)
# state [x, y, x', y']
state = opti.variable(4, num_time_steps) # x
state_weights = [1, 1]

# input [x'', y'']
inputs = opti.variable(2, num_time_steps-1) # (u) Don't care about input at goal, so -1
input_weights = [1, 1] # Increasing this this will penalize large changes in the input

# Cost function
cost = 0

# Cost = sum from i -> num_time_steps of state_importance*(reference state - state)^2
# Minimize positional error
for i in range(num_time_steps):
    cost += state_weights[0] * (target_state[0] - state[0,i])**2 
    cost += state_weights[1] * (target_state[1] - state[1,i])**2

# add to cost function: minimize controller effort
for i in range(num_time_steps-1):
    cost += input_weights[0] * (inputs[0, i])**2
    cost += input_weights[1] * (inputs[1, i])**2

# Add a cost function to avoid a circle, first num is r^2
for i in range(num_time_steps):
    x = state[0, i]
    y = state[1, i]
    cost += 10 * 4 / ((x - 1)**2 +(y - 1)**2)

for i in range(num_time_steps):
    x = state[0, i]
    y = state[1, i]
    cost += 10 * (4 * (.5**2)) / ((x - 3)**2 +(y - 3)**2)

for i in range(num_time_steps):
    x = state[0, i]
    y = state[1, i]
    cost += 10 * (4 * (.5**2)) / ((x - 1)**2 +(y - 5)**2)

opti.minimize(cost)

# Apply kinematic constraints
kinematic_constraint = KinematicConstraint()
for constraint in kinematic_constraint.get_constraints(state, inputs, dt, num_time_steps):
    opti.subject_to(constraint)

# Apply space costraint
rectangle_constraint = RectangleConstraint(1, 1, 0.5, 0.5)
for constraint in rectangle_constraint.get_constraints(state, inputs, dt, num_time_steps):
    opti.subject_to(constraint)

# Apply initial conditions
for i in range(4):
    opti.subject_to(state[i, 0] == 0)

# Apply final condition
for i in range(4):
    opti.subject_to(state[i, num_time_steps-1] == target_state[i])

# Apply velocity bounds
for i in range(num_time_steps):
    opti.subject_to(opti.bounded(-1, state[2, i], 1))
    opti.subject_to(opti.bounded(-1, state[3, i], 1))

# Apply acceleration bounds
for i in range(num_time_steps-1):
    opti.subject_to(opti.bounded(-1, inputs[0, i], 1))
    opti.subject_to(opti.bounded(-1, inputs[1, i], 1))

# Calculate solution
opti.solver('ipopt')
solution = opti.solve()

x_s, y_s, vx_s, vy_s = solution.value(state)
ax_s, ay_s = solution.value(inputs)

# print(ax_s, ay_s)

# Plot trajectory
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(x_s, y_s, label='Trajectory')
plt.scatter(target_state[0], target_state[1], color='red', label='Target')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectory')
plt.legend()

# Plot velocity profile
plt.subplot(2, 1, 2)
plt.plot(vx_s, label='X Velocity')
plt.plot(vy_s, label='Y Velocity')
plt.xlabel('Time Step')
plt.ylabel('Velocity')
plt.title('Velocity Profile')
plt.legend()

plt.tight_layout()
plt.show()

# Define obstacle coordinates
obstacle_x = [0.5, 0.5, 1.5, 1.5, 0.5]  # X coordinates of the obstacle vertices
obstacle_y = [0.5, 1.5, 1.5, 0.5, 0.5]  # Y coordinates of the obstacle vertices

# Plot trajectory on a coordinate plane with obstacle
plt.figure(figsize=(8, 6))
# plt.plot(obstacle_x, obstacle_y, 'k-', label='Obstacle', linewidth=2)  # Plot obstacle
plt.scatter(x_s, y_s, label='Trajectory', color='blue')
# Define obstacle coordinates
obstacle_x = [0.5 +2, 0.5+2, 1.5+2, 1.5+2, 0.5+2]  # X coordinates of the obstacle vertices
obstacle_y = [0.5+2, 1.5+2, 1.5+2, 0.5+2, 0.5+2]  # Y coordinates of the obstacle vertices

# plt.plot(obstacle_x, obstacle_y, 'k-', label='Obstacle', linewidth=2)  # Plot obstacle

circle1 = plt.Circle((1, 1), 1, color='r')
circle2 = plt.Circle((3, 3), .5, color='r')
circle3 = plt.Circle((1, 5), 1, color='r')

fig, ax = plt.subplots()
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)


plt.scatter(x_s, y_s, label='Trajectory', color='blue')
plt.scatter(target_state[0], target_state[1], label='Target', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectory with Obstacle')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Set equal aspect ratio
plt.show()