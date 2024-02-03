import random
import time
import pygame

from utils.render import grid_to_image, render_path
from utils.occupancy_grid import *

import config


def random_sample_node(grid: Grid, node_list: NodeList) -> Node:
    """
    Randomly sample a node on the grid that is not on an obstacle or an existent node.

    :param grid: 2D grid representing the environment.
    :type grid: Grid

    :param node_list: List of existing nodes.
    :type node_list: NodeList

    :return: Randomly sampled node.
    :rtype: Node
    """

    coord: Node = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    while coord in node_list or check_collision(grid, coord):
        coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    return coord


def initial_spawn_nodes(grid: Grid, start: Node, dist: int) -> NodeList:
    """
    Spawn one to four nodes from the start node with distance 'dist' to extend the initial search
    area of the algorithm.

    :param grid: 2D grid representing the environment.
    :type grid: Grid

    :param start: Starting node for initial spawning.
    :type start: Node

    :param dist: Distance from the start node to spawn additional nodes.
    :type dist: int

    :return: List of valid nodes spawned around the start node.
    :rtype: NodeList
    """

    nodes: NodeList = [
        (start[0] + dist, start[1] + dist),
        (start[0] + dist, start[1] - dist),
        (start[0] - dist, start[1] + dist),
        (start[0] - dist, start[1] - dist)
    ]

    valid_nodes: NodeList = []

    for node in nodes:
        if not (
                check_collision(grid, node)
                and not line_cross_check(grid, start, node)
        ):
            valid_nodes.append(node)

    return valid_nodes


def rrt_sid(grid: Grid, num_iters: int, start: Node, end: Node, dist: int, screen: pygame.Surface, out: str):
    """
    Custom version of Rapidly Exploring Random Tree (RRT) which continuously optimizes the node
    tree to minimize distance from the start node.

    :param grid: 2D grid representing the environment.
    :type grid: Grid

    :param num_iters: Number of iterations for the RRT-SID algorithm.
    :type num_iters: int

    :param start: Starting node for the pathfinding.
    :type start: Node

    :param end: Destination node for the pathfinding.
    :type end: Node

    :param dist: Distance for initial node spawning.
    :type dist: int

    :param screen: Pygame screen object for visualization (optional).
    :type screen: pygame.Surface

    :param out: Output path for saving visualization images.
    :type out: str
    """

    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    edges: Edges = {start: start}
    edges_as_list: List[Tuple[Edge, Edge]] = []
    min_distance: Path = {start: 0}

    valid_nodes: NodeList = initial_spawn_nodes(grid, start, dist)

    for node in valid_nodes:
        edges[node] = start
        edges_as_list.append((start, node))
        min_distance[node] = euclidean_distance(node, start)

    i = 0

    while i < num_iters:
        valid_node: Node = random_sample_node(grid, list(edges.keys()))

        best: Node = None
        best_dist = float('inf')

        for root in edges:
            sub_dist = euclidean_distance(root, valid_node) + min_distance[root]
            if sub_dist < best_dist \
                    and not line_cross_check(grid, root, valid_node):
                best = root
                best_dist = sub_dist

        if best is not None:
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

    best: Node = None
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
