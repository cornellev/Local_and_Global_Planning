import random
import math
import time

import pygame
from line_cross import line_cross_check
from a_star import astar

from render import image_to_grid, grid_to_image

grid = image_to_grid('./maps/example_map_binary.png')

pygame.init()
scrn = pygame.display.set_mode((len(grid), len(grid[0])))


# imp = pygame.image.load('./vis.png').convert()
# scrn.blit(imp, (0, 0))
# pygame.display.flip()


def check_collision(coord):

    return coord[0] > len(grid) - 1 or coord[1] > len(grid[1]) - 1 or  grid[coord[0]][coord[1]] == 1


def check_node(coord):
    return grid[coord[0]][coord[1]] == 5


def sample_node(nodes, root_node):
    search_radius = 30

    min_x = max(0, root_node[0] - search_radius)
    max_x = min(len(grid) - 1, root_node[0] + search_radius)
    min_y = max(0, root_node[1] - search_radius)
    max_y = min(len(grid[0]) - 1, root_node[1] + search_radius)

    # print(min_x, max_x, min_y, max_y)

    coord = random.randint(min_x, max_x), random.randint(min_y, max_y)

    # coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    while coord in nodes or check_collision(coord):
        # coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))
        coord = random.randint(min_x, max_x), random.randint(min_y, max_y)

    return coord


def find_nearest_node(node, nodes):
    min_distance = float('inf')
    closest_node = None

    for node2 in nodes:
        if node != node2:
            distance = math.sqrt((node2[0] - node[0]) ** 2 + (node2[1] - node[1]) ** 2)

            if distance < min_distance:
                if not line_cross_check(grid, node, node2):
                    min_distance = distance
                    closest_node = node2

    return closest_node


def distance(node_a, node_b):
    return (node_a[0] - node_b[0]) ** 2 + (node_a[1] - node_b[1]) ** 2


def rtt(num_iters, start, end):
    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    gamma = .7
    gamma2 = .8
    gamma_init = gamma
    found_end = False

    nodes = []
    weights = []
    weights_start = []
    edges = []

    nodes.append(start)
    weights.append(1 / distance(start, end))
    weights_start.append(1)

    for i in range(num_iters):
        print(i)
        # nodes.sort(key=lambda x: distance(x, start))

        rand = random.random()

        if rand > gamma2:
            root_node = random.choice(nodes)
        elif rand > gamma:
            root_node = random.choices(nodes, weights=weights, k=1)[0]
        else:
            root_node = random.choices(nodes, weights=weights_start, k=1)[0]
            # root_node = random.choice(nodes[-1 * min(len(nodes) - 1, 100):])

        # gamma -= gamma_init / num_iters

        node = sample_node(root_node)
        nearest_node = find_nearest_node(node, nodes)
        if nearest_node is not None:
            nodes.append(node)
            weights.append(1 / distance(node, end))
            weights_start.append(distance(node, start))
            edges.append((nearest_node, node))
            grid[node[0]][node[1]] = 5
        else:
            i += 1

        if i % 10 == 0:
            if not found_end and (find_nearest_node(end, nodes)) is not None:
                print("MEO" * 100)
                gamma = .2
                gamma2 = .8
                found_end = True

            # grid_to_image(grid, edges, 'test.png')
            # imp = pygame.image.load('./test.png').convert()
            # scrn.blit(imp, (0, 0))
            # pygame.display.flip()

    nearest_node = find_nearest_node(end, nodes)
    if nearest_node is not None:
        nodes.append(end)
        edges.append((nearest_node, end))
    else:
        print("CRITICAL ERROR")

    grid_to_image(grid, edges, 'test.png')
    return nodes


def newRTT(num_iters, start, end):
    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    nodes: {(int, int): [int, int, int]} = {}  # Node -> (dist_to_start, dist_to_end,
    # num_connections)
    edges: [((int, int), (int, int))] = []

    nodes[end] = [1 / distance(start, end), 100000000, 0]

    i = 0
    while i < num_iters:
        if (i % 50 == 0):
            print(i)

        nodes_list = list(nodes.keys())

        root_node = random.choices(nodes_list, weights=[1 / nodes[x][0] for x in nodes_list])[0]
        nearest_n = None
        next_node = None
        while nearest_n is None:
            next_node = sample_node(nodes, root_node)
            nearest_n = find_nearest_node(next_node, nodes)

            if nearest_n is not None and line_cross_check(grid, next_node, nearest_n):
                nearest_n = None

        nodes[nearest_n][2] += 1
        nodes[next_node] = [distance(start, next_node), distance(end, next_node), 1]

        edges.append((nearest_n, next_node))

        for node in nodes:
            if not line_cross_check(grid, start, node):
                print("broken")
                i = num_iters
                edges.append((start, node))

        i += 1

    grid_to_image(grid, edges, 'test.png')
    return nodes


def spawn_start(nodes_list, start, dist):
    nodes = [
        (start[0] + dist, start[1] + dist),
        (start[0] + dist, start[1] - dist),
        (start[0] - dist, start[1] + dist),
        (start[0] - dist, start[1] - dist)
    ]

    valid_nodes = []

    for node in nodes:
        if not check_collision(node) and \
                not node in nodes_list and \
                not line_cross_check(grid, start, node):
            valid_nodes.append(node)

    return valid_nodes


def spawn(nodes_list, root_node, prev_node, angle, dist):
    angle_to_root = math.atan2(root_node[1] - prev_node[1], root_node[0] - prev_node[0])
    angle_a = angle_to_root + angle
    angle_b = angle_to_root - angle

    vec_a = (math.cos(angle_a) * dist, math.sin(angle_a) * dist)
    vec_b = (math.cos(angle_b) * dist, math.sin(angle_b) * dist)
    node_a = (round(root_node[0] + vec_a[0]), round(root_node[1] + vec_a[1]))
    node_b = (round(root_node[0] + vec_b[0]), round(root_node[1] + vec_b[1]))

    valid = []

    for node in [node_a, node_b]:
        if not check_collision(node) and \
                not node in nodes_list and \
                not line_cross_check(grid, root_node, node):
            valid.append(node)

    return valid





# Tree search
# From each recently added node, attempt to spawn 2 outgoing trees at set angle and set length
# Connect new node to nearest node (only check nearby area, don't need to check entire map)
# Backtrace shortest path from the end node

def treeSearch(num_iters, start, end, angle, dist):
    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    nodes = [start]
    edges = {}
    edges_as_list = []
    not_propagated = []

    valid_nodes = spawn_start(nodes, start, dist)
    for node in valid_nodes:
        nodes.append(node)
        not_propagated.append(node)
        edges[node] = start
        edges_as_list.append((start, node))

    i = 0

    while len(not_propagated) > 0 and i < num_iters:
        root_node = not_propagated.pop(0)

        valid_nodes = spawn(nodes, root_node, edges[root_node], angle, dist)
        for node in valid_nodes:
            nodes.append(node)
            not_propagated.append(node)
            edges[node] = root_node
            edges_as_list.append((root_node, node))

            grid_to_image(grid, edges_as_list, 'test.png')
            imp = pygame.image.load('./test.png').convert()
            scrn.blit(imp, (0, 0))
            pygame.display.flip()
            time.sleep(.5)

        i += 1

    nearest_node = find_nearest_node(end, nodes)
    if nearest_node is not None:
        nodes.append(end)
        edges[end] = nearest_node
        edges_as_list.append((nearest_node, end))
    else:
        print("CRITICAL ERROR")

    grid_to_image(grid, edges_as_list, 'test.png')

    return nodes, edges


# nodes = newRTT(400, (10, 10), (300, 300))
# nodes = rtt(400, (10, 10), (300, 300))
nodes, edges = treeSearch(400, (10, 10), (300, 300), math.radians(25), 50)
# print(astar(nodes, (10, 10), (300, 300), distance))
