# Bresenham line crossing algorithm
def line_cross_check(grid, nodeA, nodeB):
    x0, y0 = nodeA
    x1, y1 = nodeB

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x_sign = 1 if x1 > x0 else -1
    y_sign = 1 if y1 > y0 else -1

    if dx > dy:
        err = dx / 2.0
        while x0 != x1:
            if 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid):
                if grid[y0][x0] == 1:
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
                if grid[y0][x0] == 1:
                    return True
            err -= dx
            if err < 0:
                x0 += x_sign
                err += dy
            y0 += y_sign

    # Check the last point
    if 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid):
        if grid[y0][x0] == 1:
            return True

    return False
