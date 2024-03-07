import random


def add_costs(grid, center, initial_cost):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    grid[center[0]][center[1]] = float('inf')

    # Calculate the maximum distance from the center to the edges of the grid
    max_distance = max(abs(center[0] - 0), abs(center[0] - (rows - 1)), abs(center[1] - 0),
                       abs(center[1] - (cols - 1)))

    # Iterate over each layer of cells from the center outward
    for distance in range(max_distance + 1):
        # Calculate the cost for the current layer
        current_cost = initial_cost / (2 ** (distance + 1))

        # Iterate over each cell in the current layer
        for i in range(max(0, center[0] - distance), min(rows, center[0] + distance + 1)):
            for j in range(max(0, center[1] - distance), min(cols, center[1] + distance + 1)):
                # Add the current cost to the cell in the grid
                grid[i][j] += current_cost


def add_goal_costs(grid, center, initial_cost):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    grid[center[0]][center[1]] = float('-inf')

    # Calculate the maximum distance from the center to the edges of the grid
    max_distance = max(abs(center[0] - 0), abs(center[0] - (rows - 1)), abs(center[1] - 0),
                       abs(center[1] - (cols - 1)))

    # Iterate over each layer of cells from the center outward
    for distance in range(max_distance + 1):
        # Calculate the cost for the current layer
        current_cost = initial_cost / (2 ** (distance + 1))

        # Iterate over each cell in the current layer
        for i in range(max(0, center[0] - distance), min(rows, center[0] + distance + 1)):
            for j in range(max(0, center[1] - distance), min(cols, center[1] + distance + 1)):
                # Add the current cost to the cell in the grid
                grid[i][j] += current_cost


# # Example usage:
# grid = [[0] * 10 for _ in range(10)]
# initial_cost = 10
# # obstacles = [(7, 7), (1, 1), (9, 0)]
# obstacles = []
#
# for i in range(50):
#     x = random.randint(0, 9)
#     y = random.randint(0, 9)
#     obstacles.append((x, y))
#
# for i in obstacles:
#     add_costs(grid, i, initial_cost)
#
# # Printing the resulting grid with obstacle in a different color
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i, j) in obstacles:
#             print('\033[91m' + str(grid[i][j]) + '\033[0m', end=' ')  # Print obstacle in red color
#         else:
#             print(grid[i][j], end=' ')
#     print()

import random
import time


def dist(point_a, point_b):
    return ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) ** .5


#
#
# def find_nearest_obstacle(grid, start_point):
#     while (grid[start_point[0]][start_point[1]] != float('inf')):
#         options = [(x, y) for x in
#                    range(max(0, start_point[0] - 1), min(len(grid) - 1, start_point[0] + 1) + 1) for
#                    y in
#                    range(max(0, start_point[1] - 1), min(len(grid[0]) - 1, start_point[1] + 1) + 1)]
#
#         best_option = options[0]
#         best_cost = grid[options[0][0]][options[0][1]]
#         unchanged = True
#
#         for i in options:
#             cost = grid[i[0]][i[1]]
#
#             if cost > best_cost:
#                 unchanged = False
#                 best_option = i
#                 best_cost = cost
#             elif cost < best_cost:
#                 unchanged = False
#
#         if unchanged:
#             best_option = random.choice(options)
#
#         start_point = best_option
#
#     return start_point
#
#
# def test_nearest_obstacle(grid, start_point, obstacles):
#     nearest_obstacle = None
#     best_cost = float('inf')
#
#     for obstacle in obstacles:
#         cost = dist(obstacle, start_point)
#         if cost < best_cost:
#             nearest_obstacle = obstacle
#             best_cost = cost
#
#     obs = find_nearest_obstacle(grid, start_point)
#
#     return dist(start_point, obs) == best_cost, obs, nearest_obstacle
#
#
# num_tests = 0
# num_passed = 0
#
# for x in range(len(grid)):
#     for y in range(len(grid[0])):
#         num_tests += 1
#         out, put, real = test_nearest_obstacle(grid, (x, y), obstacles)
#         if not out:
#             print(
#                 f"{(x, y)} gave {put} with a cost of {dist((x, y), put)}. The real soln was {real} with a cost of {dist((x, y), real)}.")
#         num_passed += out
#
# print(num_passed / num_tests)
# print("done")

# ___

grid = [[0] * 1000 for _ in range(1000)]

obstacles = []

# Add square obstacles
for i in range(125, 175):
    for j in range(125, 175):
        obstacles.append((i, j))

for i in range(225, 275):
    for j in range(225, 275):
        obstacles.append((i, j))

for i in range(325, 475):
    for j in range(325, 475):
        obstacles.append((i, j))

goal = (500, 500)


def cost_function(x, y):
    cost = 0
    for i in obstacles:
        dist_ = dist((x, y), i)

        if not dist_:
            return -100000000

        cost += -100 * 1 / dist_

    cost += -1000 * dist((x, y), goal)

    return cost


start = (0, 0)
grid[goal[0]][goal[1]] = float('-inf')

# initial_cost = -1000
# goal_cost = 10000
#
# start = (0, 0)
#
# print("here")
#
# for i in obstacles:
#     add_costs(grid, i, initial_cost)
#     print("here")
#
# add_goal_costs(grid, goal, goal_cost)
#
# print("here")

path = []


def find_nearest_goal(grid, start_point):
    while grid[start_point[0]][start_point[1]] != float('-inf'):
        options = [(x, y) for x in
                   range(max(0, start_point[0] - 1), min(len(grid) - 1, start_point[0] + 1) + 1) for
                   y in
                   range(max(0, start_point[1] - 1), min(len(grid[0]) - 1, start_point[1] + 1) + 1)]

        best_option = options[0]
        best_cost = cost_function(options[0][0], options[0][1])
        unchanged = True

        for i in options:
            cost = cost_function(i[0], i[1])

            if cost > best_cost:
                unchanged = False
                best_option = i
                best_cost = cost
            elif cost < best_cost:
                unchanged = False

        if unchanged:
            best_option = random.choice(options)

        start_point = best_option
        print(start_point)
        path.append(start_point)

    return start_point


find_nearest_goal(grid, start)

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i, j) in obstacles:
#             print('\033[91m' + str(grid[i][j]) + '\033[0m', end=' ')  # Print obstacle in red color
#         elif i == goal[0] and j == goal[1]:
#             print('\033[92m' + str(grid[i][j]) + '\033[0m', end=' ')  # Print goal in green color
# else:
#     print(grid[i][j], end=' ')
# print()

# Chart the goal and obstacles and path on matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for i in obstacles:
    ax.plot(i[0], i[1], 'ro')

for i in path:
    ax.plot(i[0], i[1], 'bo')

ax.plot(goal[0], goal[1], 'go')

plt.show()
