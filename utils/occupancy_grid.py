from type_hints.types import *


def line_cross_check(grid: Grid, node_a: Node, node_b: Node) -> bool:
    """
    Uses Bresenham line crossing algorithm to check if the line created between two nodes
    intersects any obstacles.
    """

    x0, y0 = node_a
    x1, y1 = node_b

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x_sign = 1 if x1 > x0 else -1
    y_sign = 1 if y1 > y0 else -1

    if dx > dy:
        err = dx / 2.0
        while x0 != x1:
            if 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid):
                if grid[y0][x0] == 1 or grid[y0][x0] == 2:
                    return True
            err -= dy
            if err < 0:
                y0 += y_sign
                err += dx
            x0 += x_sign
    else:
        err = dy / 2.0
        while y0 != y1:
            if 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid):
                if grid[y0][x0] == 1 or grid[y0][x0] == 2:
                    return True
            err -= dx
            if err < 0:
                x0 += x_sign
                err += dy
            y0 += y_sign

    if 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid):
        if grid[y0][x0] == 1 or grid[y0][x0] == 2:
            return True

    return False


def check_collision(grid: Grid, node: Node) -> bool:
    """
    Returns True if a node is in the same area as an obstacle.
    """
    return (
            node[0] < 0
            or node[0] > len(grid) - 1
            or node[1] < 0
            or node[1] > len(grid[0]) - 1
            or grid[node[0]][node[1]] == 1
            or grid[node[0]][node[1]] == 2

    )


def euclidean_distance(node_a: Node, node_b: Node) -> float:
    """
    Returns the Euclidean Distance between two nodes as a float.
    """
    return ((node_a[0] - node_b[0]) ** 2 + (node_a[1] - node_b[1]) ** 2) ** .5


def find_nearest_node(grid: Grid, node_list: NodeList, node: Node) -> Node or None:
    """
    Returns the closest node in a NodeList to a given Node or None if no valid Nodes are found.
    """
    best = None
    best_dist = float('inf')

    for root in node_list:
        dist = euclidean_distance(root, node)
        if dist < best_dist and not line_cross_check(grid, root, node):
            best = root
            best_dist = dist

    return best
