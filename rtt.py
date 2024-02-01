import random
import math
import pygame
from line_cross import line_cross_check

from render import image_to_grid, grid_to_image

grid = image_to_grid('./maps/example_map_binary.png')


pygame.init()
scrn = pygame.display.set_mode((len(grid), len(grid[0])))
# imp = pygame.image.load('./vis.png').convert()
# scrn.blit(imp, (0, 0))
# pygame.display.flip()


def check_collision(coord):
    return grid[coord[0]][coord[1]] == 1


def check_node(coord):
    return grid[coord[0]][coord[1]] == 5


def sample_node(root_node):
    search_radius = 80

    min_x = max(0, root_node[0] - search_radius)
    max_x = min(len(grid) - 1, root_node[0] + search_radius)
    min_y = max(0, root_node[1] - search_radius)
    max_y = min(len(grid[0]) - 1, root_node[1] + search_radius)

    # print(min_x, max_x, min_y, max_y)

    coord = random.randint(min_x, max_x), random.randint(min_y, max_y)




    # coord = (random.randint(0, len(grid) - 1), random.randint(0, len(grid[0]) - 1))

    while check_node(coord) or check_collision(coord):
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
    return (node_a[0] - node_b[0])**2 + (node_a[1] - node_b[1])**2

def rtt(num_iters, start, end):
    grid[start[0]][start[1]] = 3
    grid[end[0]][end[1]] = 4

    gamma = .9
    gamma_init = gamma

    nodes = []
    weights = []
    edges = []

    nodes.append(start)
    weights.append(1 / distance(start, end))

    for i in range(num_iters):
        print(i)
        # nodes.sort(key=lambda x: distance(x, end), reverse=True)
        # root_node = random.choice(nodes[-1 * min(len(nodes) - 1, 100):])
        if random.random() > gamma:
            root_node = random.choices(nodes, weights=weights, k=1)[0]
        else:
            root_node = random.choice(nodes)

        # gamma -= gamma_init / num_iters

        node = sample_node(root_node)
        nearest_node = find_nearest_node(node, nodes)
        if nearest_node is not None:
            nodes.append(node)
            weights.append(1 / distance(node, end))
            edges.append((nearest_node, node))
            grid[node[0]][node[1]] = 5
        else:
            i += 1

        if (i%10 == 0):
            if (find_nearest_node(end, nodes)) is not None:
                print("MEO")
                gamma = .3

            grid_to_image(grid, edges, 'test.png')
            imp = pygame.image.load('./test.png').convert()
            scrn.blit(imp, (0, 0))
            pygame.display.flip()



    nearest_node = find_nearest_node(end, nodes)
    if nearest_node is not None:
        nodes.append(end)
        edges.append((nearest_node, end))
    else:
        print("CRITICAL ERROR")

    grid_to_image(grid, edges, 'test.png')


rtt(4000, (10, 10), (300, 300))
