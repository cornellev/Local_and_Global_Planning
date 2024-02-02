import math
import random
import time

import pygame

from utils.line_cross import line_cross_check
from utils.render import grid_to_image, render_path

import config


def check_collision(grid, coord):
    return coord[0] > len(grid) - 1 or coord[1] > len(grid[1]) - 1 or grid[coord[0]][coord[1]] == 1


def sample_node(grid, nodes):
    coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    while coord in nodes or check_collision(grid, coord):
        coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    return coord


def distance(node_a, node_b):
    return ((node_a[0] - node_b[0]) ** 2 + (node_a[1] - node_b[1]) ** 2) ** .5


def spawn_start(grid, nodes_list, start, dist):
    nodes = [
        (start[0] + dist, start[1] + dist),
        (start[0] + dist, start[1] - dist),
        (start[0] - dist, start[1] + dist),
        (start[0] - dist, start[1] - dist)
    ]

    valid_nodes = []

    for node in nodes:
        if not check_collision(grid, node) and \
                not node in nodes_list and \
                not line_cross_check(grid, start, node):
            valid_nodes.append(node)

    return valid_nodes


def spawn(grid, root_node, prev_node, angle, min_dist):
    valid = []

    angle_to_root = math.atan2(root_node[1] - prev_node[1], root_node[0] - prev_node[0])
    angle_a = angle_to_root + angle
    angle_b = angle_to_root - angle

    magnitude = min_dist

    vec_a = (math.cos(angle_a), math.sin(angle_a))
    a = (vec_a[0] * magnitude, vec_a[1] * magnitude)
    node_a = (round(root_node[0] + a[0]), round(root_node[1] + a[1]))

    while (not node_a[0] > len(grid) - 1
           and not node_a[1] > len(grid[0]) - 1
           and not node_a[0] < 0
           and not node_a[1] < 0
           and not check_collision(grid, node_a)
           and not line_cross_check(grid, root_node, node_a)
    ):
        magnitude += 1
        a = (vec_a[0] * magnitude, vec_a[1] * magnitude)
        node_a = (round(root_node[0] + a[0]), round(root_node[1] + a[1]))

    if magnitude != min_dist:
        valid.append(
            (round(vec_a[0] * (magnitude - 1) / 2) + root_node[0], round(vec_a[1] * (magnitude -
                                                                                     1) / 2) +
             root_node[1]))

    magnitude = min_dist
    vec_b = (math.cos(angle_b), math.sin(angle_b))
    b = (vec_b[0] * magnitude, vec_b[1] * magnitude)
    node_b = (round(root_node[0] + b[0]), round(root_node[1] + b[1]))

    while (not node_b[0] > len(grid) - 1
           and not node_b[1] > len(grid[0]) - 1
           and not node_b[0] < 0
           and not node_b[1] < 0
           and not check_collision(grid, node_b)
           and not line_cross_check(grid, root_node, node_b)
    ):
        magnitude += 1
        b = (vec_b[0] * magnitude, vec_b[1] * magnitude)
        node_b = (round(root_node[0] + b[0]), round(root_node[1] + b[1]))

    if magnitude != min_dist:
        valid.append(
            (round(vec_b[0] * (magnitude - 1) / 2) + root_node[0], round(vec_b[1] * (magnitude -
                                                                                     1) / 2) +
             root_node[1]))

    return valid


# Tree search
# From each recently added node, attempt to spawn 2 outgoing trees at set angle and set length
# Connect new node to nearest node (only check nearby area, don't need to check entire map)
# Backtrace shortest path from the end node

def rrt_sid(grid, num_iters, start, end, dist, screen, out):
    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    edges = {start: start}
    edges_as_list = []
    not_propagated = []
    min_distance = {start: 0}

    valid_nodes = spawn_start(grid, edges.keys(), start, dist)

    for node in valid_nodes:
        not_propagated.append(node)
        edges[node] = start
        edges_as_list.append((start, node))
        min_distance[node] = distance(node, start)

    i = 0

    while len(not_propagated) > 0 and i < num_iters:
        valid_node = sample_node(grid, list(edges.keys()))

        best = None
        best_dist = float('inf')

        for root in edges:
            sub_dist = distance(root, valid_node) + min_distance[root]
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
        sub_dist = distance(root, end) + min_distance[root]
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
