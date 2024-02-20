from casadi import *
from matplotlib import pyplot as plt

from local_sim.obstacle import Obstacle

dT = .1
T = 10
N = int(T/dT)

optimizer = Opti()

start_state = [0, 0, 0, 0]
end_state = [4, 4, 0, 0]

obstacles = [
    Obstacle(1.5, 1.5, 1),  # x, y, radius
    Obstacle(2.5, 2.5, .3),  # x, y, radius
    Obstacle(3, 2, .5),  # x, y, radius
    Obstacle(2.5, 4, .3)  # x, y, radius
]

obstacle_padding = .5

# Decision variables
state = optimizer.variable(4, N)
u = optimizer.variable(2, N-1)

# Set up cost function
cost = 0

for i in range(N):
    cost += (state[0, i] - end_state[0])**2
    cost += (state[1, i] - end_state[1])**2

for i in range(N-1):
    cost += casadi.fabs(u[0, i])**2
    cost += casadi.fabs(u[1, i])**2

optimizer.minimize(cost)

# Set up constraints
for i in range(N - 1):
    optimizer.subject_to(state[2, i + 1] == state[2, i] + u[0, i] * dT)
    optimizer.subject_to(state[3, i + 1] == state[3, i] + u[1, i] * dT)
    optimizer.subject_to(state[0, i + 1] == state[0, i] + state[2, i] * dT)
    optimizer.subject_to(state[1, i + 1] == state[1, i] + state[3, i] * dT)

for obstacle in obstacles:
    for i in range(N):
        x = state[0, i]
        y = state[1, i]
        dist_from_center = (x - obstacle.x) ** 2 + (y - obstacle.y) ** 2

        optimizer.subject_to(dist_from_center >= (obstacle.radius ** 2 + obstacle_padding ** 2))

for i in range(4):
    optimizer.subject_to(state[i, 0] == 0)

for i in range(4):
    optimizer.subject_to(state[i, N - 1] == end_state[i])

# Apply velocity bounds
for i in range(N):
    optimizer.subject_to(optimizer.bounded(-1, state[2, i], 1))
    optimizer.subject_to(optimizer.bounded(-1, state[3, i], 1))

# Apply acceleration bounds
for i in range(N - 1):
    optimizer.subject_to(optimizer.bounded(-1, u[0, i], 1))
    optimizer.subject_to(optimizer.bounded(-1, u[1, i], 1))


# Calculate solution
opts = {'ipopt.print_level': 0}
optimizer.solver('ipopt', opts)
solution = optimizer.solve()

x_s, y_s, vx_s, vy_s = solution.value(state)
ax_s, ay_s = solution.value(u)

# print(ax_s, ay_s)

# Plot trajectory
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(x_s, y_s, label='Trajectory')
plt.scatter(end_state[0], end_state[1], color='red', label='Target')
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

# Plot trajectory on a coordinate plane with obstacle
plt.figure(figsize=(8, 6))
plt.scatter(x_s, y_s, label='Trajectory', color='blue')
plt.scatter(x_s, y_s, label='Trajectory', color='blue')
plt.scatter(end_state[0], end_state[1], label='Target', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectory with Obstacle')
plt.legend()
plt.grid(True)
plt.axis('equal')  # Set equal aspect ratio

for obstacle in obstacles:
    obstacle.plot()

plt.show()






