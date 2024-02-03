import pygame

from type_hints.types import Grid
from utils.render import image_to_grid
import config

grid: Grid = image_to_grid(config.map_path)

screen = None
if config.debug:
    pygame.init()
    screen = pygame.display.set_mode((len(grid[0]), len(grid)))

config.algo_options[config.algo](
    grid,
    config.iters,
    config.start_node,
    config.end_node,
    config.initial_generate_dist,
    screen,
    config.out_path
)
