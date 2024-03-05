import time

import pygame

from local_sim.obstacle import Obstacle
from local_sim.path import LocalPlanner
from global_sim.algorithm import rrt_sid, rrt_star
from type_hints.types import Grid
from utils.render import image_to_grid, render_local_path_on_image, render_circle_on_image, \
    clean_padding
import config

start_time = time.time()

# ----------------- SETUP ----------------- #

# Generate a 800 x 800 grid filled with zeroes
grid: Grid = [[0 for _ in range(800)] for _ in range(800)]

obstacles = [
    (200, 200, 20),
    (300, 300, 20),
    (200, 150, 10),
    (150, 200, 40),
    (175, 630, 10),
    (630, 175, 10),
]

# Add circular obstacles to the grid as 1s, and add padding
for obstacle in obstacles:
    min_x = max(0, obstacle[0] - obstacle[2] - config.padding)
    max_x = min(800, obstacle[0] + obstacle[2] + config.padding)
    min_y = max(0, obstacle[1] - obstacle[2] - config.padding)
    max_y = min(800, obstacle[1] + obstacle[2] + config.padding)

    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            dist_to_center = ((i - obstacle[0]) ** 2 + (j - obstacle[1]) ** 2) ** .5

            if dist_to_center < obstacle[2]:
                grid[i][j] = 1
            elif dist_to_center < obstacle[2] + config.padding:
                grid[i][j] = 2

# ----------------- GLOBAL PLANNER ----------------- #
#
global_path = {"rrt_sid": rrt_sid, "rrt_star": rrt_star}[config.algo](
    grid,
    config.iters,
    config.start_node,
    config.end_node,
    config.initial_generate_dist,
    screen=None,
    out='test.png'
)

