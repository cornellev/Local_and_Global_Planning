import math
import random
import time
import pygame

from utils.render import grid_to_image, render_path
from utils.occupancy_grid import *

import config


def random_sample_node(grid: Grid, node_list: NodeList) -> Node:
    """
    Randomly sample a node on the grid that is not on an obstacle or an existent node.
    """
    coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    while coord in node_list or check_collision(grid, coord):
        coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    return coord


def initial_spawn_nodes(grid: Grid, start: Node, dist: int) -> NodeList:
    """
    Spawn one to four nodes from the start node with distance 'dist' to extend the initial search
    area of the algorithm.
    """
    nodes = [
        (start[0] + dist, start[1] + dist),
        (start[0] + dist, start[1] - dist),
        (start[0] - dist, start[1] + dist),
        (start[0] - dist, start[1] - dist)
    ]

    valid_nodes = []

    for node in nodes:
        if not (
                check_collision(grid, node)
                and not line_cross_check(grid, start, node)
        ):
            valid_nodes.append(node)

    return valid_nodes


def rrt_sid(grid: Grid, num_iters: int, start: Node, end: Node, dist: int, screen, out: str):
    """
    Custom version of Rapidly Exploring Random Tree (RRT) which continuously optimizes the node
    tree to minimize distance from the start node.
    """

    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    edges = {start: start}
    edges_as_list = []
    not_propagated = []
    min_distance = {start: 0}

    valid_nodes = initial_spawn_nodes(grid, start, dist)

    for node in valid_nodes:
        not_propagated.append(node)
        edges[node] = start
        edges_as_list.append((start, node))
        min_distance[node] = euclidean_distance(node, start)

    i = 0

    while len(not_propagated) > 0 and i < num_iters:
        valid_node = random_sample_node(grid, list(edges.keys()))

        best = None
        best_dist = float('inf')

        for root in edges:
            sub_dist = euclidean_distance(root, valid_node) + min_distance[root]
            if sub_dist < best_dist \
                    and not line_cross_check(grid, root, valid_node):
                best = root
                best_dist = sub_dist

        if best is not None:
            not_propagated.append(valid_node)
            edges[valid_node] = best
            min_distance[valid_node] = best_dist
            edges_as_list.append((best, valid_node))

        if config.debug and i % config.debug_iters == 0:
            print(i)
            grid_to_image(grid, edges_as_list, out)
            imp = pygame.image.load(out).convert()
            screen.blit(imp, (0, 0))
            pygame.display.flip()
            time.sleep(config.debug_time)

        i += 1

    best = None
    best_dist = float('inf')

    for root in edges:
        sub_dist = euclidean_distance(root, end) + min_distance[root]
        if sub_dist < best_dist \
                and not line_cross_check(grid, root, end):
            best = root
            best_dist = sub_dist

    if best is None:
        print("CRITICAL ERROR, could not reach end node.")
    else:
        edges[end] = best
        edges_as_list.append((best, end))

    render_path(grid, edges, edges_as_list, out)
