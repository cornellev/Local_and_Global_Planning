import time

import pygame

from local_sim.path import LocalPlanner
from global_sim.algorithm import rrt_sid, rrt_star
from type_hints.types import Grid
from utils.occupancy_grid import waypoints_gen
from utils.render import image_to_grid, render_local_path_on_image
import config

start_time = time.time()

grid: Grid = image_to_grid(config.map_path, reverse_colors=config.map_bw_reverse)

screen = None
if config.debug:
    pygame.init()
    screen = pygame.display.set_mode((len(grid[0]), len(grid)))

pygame.init()
screen = pygame.display.set_mode((len(grid[0]), len(grid)))

algo_options = {
    "rrt_sid": rrt_sid,
    "rrt_star": rrt_star
}

global_path = algo_options[config.algo](
    grid,
    config.iters,
    config.start_node,
    config.end_node,
    config.initial_generate_dist,
    screen,
    config.out_path
)

for i in range(len(global_path)):
    global_path[i] = (global_path[i][0], global_path[i][1], 0, 0)

global_path = waypoints_gen(global_path, 20)

local_planner = LocalPlanner(.5, 5)
local_path = []

render_local_path_on_image([], config.out_path, 'test.png')

for i in range(len(global_path) - 1):
    solution, state, u = local_planner.find_path(global_path[i], global_path[i + 1], [])
    path = local_planner.get_path_coords(solution, state)
    global_path[i+1] = path[-1]
    local_path.extend(path)

    render_local_path_on_image(path, "test.png", "test.png")
    imp = pygame.image.load("test.png").convert()
    screen.blit(imp, (0, 0))
    pygame.display.flip()

x = input()

print("Finished in:")
print(f"{time.time() - start_time} seconds.")