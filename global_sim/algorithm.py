import random
import time

import numpy as np
import pygame

from utils.render import grid_to_image, render_path, render_path_new
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


def rrt_star(grid: Grid, num_iters: int, start: Node, end: Node, dist: int, screen=None, out: str = ""):
    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    nodes: Dict[Node, Node] = {start: start}
    edges_as_list: List[Tuple[Node, Node]] = []
    cost: Dict[Node, float] = {start: 0.0}

    i = 0

    while i < num_iters:
        valid_node: Node = random_sample_node(grid, list(nodes.keys()))

        nearest_node, nearest_node_cost = nearest_neighbor(valid_node, nodes, cost)

        new_node = steer(nearest_node, valid_node, dist)
        if new_node is not None and not (check_collision(grid, new_node) or line_cross_check(grid, nearest_node, new_node)):
            near_nodes = near_neighbors(new_node, nodes, max_dist=dist)
            min_cost_node = nearest_node
            min_cost = nearest_node_cost + euclidean_distance(nearest_node, new_node)

            for near_node in near_nodes:
                cur_cost = cost[near_node] + euclidean_distance(near_node, new_node)
                if cur_cost < min_cost and not line_cross_check(grid, near_node, new_node):
                    min_cost_node = near_node
                    min_cost = cur_cost

            nodes[new_node] = min_cost_node
            edges_as_list.append((min_cost_node, new_node))
            cost[new_node] = min_cost

            # Rewiring step
            for near_node in near_nodes:
                potential_cost = cost[new_node] + euclidean_distance(new_node, near_node)
                if potential_cost < cost[near_node] and not line_cross_check(grid, new_node, near_node):
                    nodes[near_node] = new_node
                    edges_as_list.append((new_node, near_node))
                    cost[near_node] = potential_cost

            if config.debug and i % config.debug_iters == 0:  # Visualization (optional)
                print(i)
                grid_to_image(grid, edges_as_list, out)
                imp = pygame.image.load(out).convert()
                screen.blit(imp, (0, 0))
                pygame.display.flip()
                time.sleep(0.1)

        i += 1

    nearest_end, _ = nearest_neighbor(end, nodes, cost)
    nodes[end] = nearest_end
    edges_as_list.append((nearest_end, end))

    # Final path extraction
    path = extract_path(nodes, start, end)
    render_path_new(grid, path, edges_as_list, out)


def nearest_neighbor(target_node, nodes, cost):
    nearest_node = min(nodes, key=lambda node: euclidean_distance(node, target_node))
    nearest_node_cost = cost[nearest_node]
    return nearest_node, nearest_node_cost


def steer(from_node: Node, to_node: Node, max_distance: int) -> Node:
    direction = np.array(to_node) - np.array(from_node)
    distance_to_target = np.linalg.norm(direction)
    if distance_to_target > max_distance:
        normalized_direction = direction / distance_to_target
        new_node = from_node + max_distance * normalized_direction
        return tuple(map(int, new_node))
    else:
        return to_node


def near_neighbors(target_node: Node, nodes, max_dist: int):
    return [node for node in nodes if euclidean_distance(node, target_node) <= max_dist]


def extract_path(nodes, start: Node, end: Node):
    path = []
    current = end
    while current != start:
        path.append((nodes[current], current))
        current = nodes[current]
    return path
