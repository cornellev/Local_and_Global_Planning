import time

import pygame

from local_sim.obstacle import Obstacle
from local_sim.path import LocalPlanner
from global_sim.algorithm import rrt_sid, rrt_star
from type_hints.types import Grid
from utils.render import image_to_grid, render_local_path_on_image
import config

start_time = time.time()

grid: Grid = image_to_grid(config.map_path, reverse_colors=config.map_bw_reverse)

screen = None
if config.debug:
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

current_position = global_path[0]
target_waypoint = global_path[1]

render_local_path_on_image([], config.out_path, 'test.png')

total_dist = (target_waypoint[0] - current_position[0]) ** 2 + (target_waypoint[1] -
                                                                current_position[1]) ** 2

obstacles = []
search_radius = 10

# Search in area near waypoints for obstacles
for i in range(-search_radius, search_radius, 3):
    for j in range(-search_radius, search_radius):
        if 0 <= current_position[0] + i < len(grid) and 0 <= current_position[1] + j < len(grid[0]):
            if grid[current_position[0] + i][current_position[1] + j] == 1:
                obstacles.append(Obstacle(current_position[0] + i, current_position[1] + j, .5))

while (current_position[0], current_position[1]) != (global_path[-1][0], global_path[-1][1]):
    local_planner = LocalPlanner(.05, .25)

    solution, state, u = local_planner.find_path(current_position, target_waypoint, total_dist, obstacles)
    path = local_planner.get_path_coords(solution, state)
    current_position = path[-1]

    if (current_position[0] - target_waypoint[0]) ** 2 + (
            current_position[1] - target_waypoint[1]) ** 2 < 25**2:
        if global_path.index(target_waypoint) + 1 < len(global_path):
            target_waypoint = global_path[global_path.index(target_waypoint) + 1]
        else:
            break

        total_dist = ((target_waypoint[0] - current_position[0]) ** 2 + (target_waypoint[1] -
                                                                         current_position[1])) ** 2

    render_local_path_on_image(path, 'test.png', 'test.png')
    if config.debug:
        imp = pygame.image.load('test.png').convert()
        screen.blit(imp, (0, 0))
        pygame.display.flip()
