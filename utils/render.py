from PIL import Image, ImageDraw

import config
from type_hints.types import Grid, Edges, Path
from utils.spline import smooth_path, convert_to_coordinates

render_lines = True

white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red = (255, 0, 0, 100)
blue = (0, 0, 255, 100)
purple = (83, 11, 120, 150)
purple2 = (106, 12, 153, 100)
green = (0, 255, 0, 100)
pink = (255, 192, 203, 256)

color_mapping = {
    0: black,
    1: white,
    2: pink,
    3: black,
    4: black,
    5: black
}


def image_to_grid(map_path: str, reverse_colors: bool = False) -> Grid:
    """
    Converts a provided map path to a Grid.

    :param map_path: Path to a valid map (only black and white image).
    :type map_path: str

    :param reverse_colors: Reverse the colors for obstacle vs free territory.
    :type reverse_colors: bool

    :return: 2D grid representing the environment.
    :rtype: Grid
    """

    img = Image.open(map_path)

    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    for pixel_row in pixels:
        for pixel in range(len(pixel_row)):
            if pixel_row[pixel] != 2:
                if all([x > 150 for x in pixel_row[pixel]]):
                    pixel_row[pixel] = 1 if not reverse_colors else 0
                else:
                    pixel_row[pixel] = 0 if not reverse_colors else 1

    for pixel_row in range(len(pixels)):
        for pixel in range(len(pixels[pixel_row])):
            if pixels[pixel_row][pixel] == 1:
                top = max(0, pixel_row - config.padding)
                bottom = min(pixel_row + config.padding, len(pixels) - 1)
                left = max(0, pixel - config.padding)
                right = min(pixel + config.padding, len(pixels[0]))

                for j in range(top, bottom):
                    for k in range(left, right):
                        if pixels[j][k] != 1:
                            pixels[j][k] = 2

    return pixels


def grid_to_image(grid: Grid, edges: Edges, output_path: str):
    """
    Writes a given grid and set of edges to an image.

    :param grid: 2D grid representing the environment.
    :type grid: Grid

    :param edges: List of node pairs representing edges to be drawn on the image.
    :type edges: Edges

    :param output_path: Path to save the output image to.
    :type output_path: str
    """

    height = len(grid)
    width = len(grid[0])

    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(new_img)
    start = (0, 0)
    end = (0, 0)

    for x in range(height):
        for y in range(width):
            new_img.putpixel((y, x), color_mapping.get(grid[x][y], black))
            if grid[x][y] == 3:
                start = (x, y)
            if grid[x][y] == 4:
                end = (x, y)

    if render_lines:
        for start_node, end_node in edges:
            draw.line([start_node, end_node], fill=purple, width=2)  # Change fill and width as needed

    box = (start[0] - 3, start[1] - 3, start[0] + 3, start[1] + 3)
    draw.ellipse(box, outline="red", width=3)
    box = (end[0] - 3, end[1] - 3, end[0] + 3, end[1] + 3)
    draw.ellipse(box, outline="green", width=5)

    new_img.save(output_path)


def render_path(grid: Grid, path: Path, edges: Edges, output_path: str):
    """
    Renders a grid and edges along with the optimal path to an output file.

    :param grid: 2D grid representing the environment.
    :type grid: Grid

    :param path: Dictionary representing the optimal path from end to start.
    :type path: Path

    :param edges: List of node pairs representing edges to be drawn on the image.
    :type edges: Edges

    :param output_path: Path to save the output image to.
    :type output_path: str
    """

    height = len(grid)
    width = len(grid[0])

    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(new_img)
    start = (0, 0)
    end = (0, 0)

    for x in range(height):
        for y in range(width):
            new_img.putpixel((y, x), color_mapping.get(grid[x][y], black))
            if grid[x][y] == 3:
                start = (x, y)
            if grid[x][y] == 4:
                end = (x, y)

    if render_lines:
        for start_node, end_node in edges:
            draw.line([start_node, end_node], fill=purple, width=2)  # Change fill and width as needed

        waypoints = []

        current = end
        while current != start:
            draw.line([current, path[current]], fill=(255, 0, 0, 255), width=2)
            current = path[current]
            waypoints.append(list(current))

        smoothed_path = [(round(x[0]), round(x[1])) for x in convert_to_coordinates(smooth_path(list(
            end), list(start), waypoints))]

        for coord in range(len(smoothed_path[:-1])):
            draw.line([smoothed_path[coord], smoothed_path[coord + 1]], fill=blue, width=2)

    box = (start[0] - 3, start[1] - 3, start[0] + 3, start[1] + 3)
    draw.ellipse(box, outline="red", width=3)
    box = (end[0] - 3, end[1] - 3, end[0] + 3, end[1] + 3)
    draw.ellipse(box, outline="green", width=5)

    new_img.save(output_path)


def render_dict_path(grid: Grid, path, edges, output_path: str):
    """
    Renders a grid, edges, and the optimal path to an output file.

    :param grid: 2D grid representing the environment.
    :type grid: Grid

    :param path: List of coordinate pairs representing the optimal path from start to end.
    :type path: List[Tuple[Node, Node]]

    :param edges: List of coordinate pairs representing edges to be drawn on the image.
    :type edges: List[Tuple[Node, Node]]

    :param output_path: Path to save the output image.
    :type output_path: str
    """
    height = len(grid)
    width = len(grid[0])

    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(new_img)
    start = (0, 0)
    end = (0, 0)

    for x in range(height):
        for y in range(width):
            new_img.putpixel((y, x), color_mapping.get(grid[x][y], black))
            if grid[x][y] == 3:
                start = (x, y)
            if grid[x][y] == 4:
                end = (x, y)

    if render_lines:
        for start_node, end_node in edges:
            draw.line([start_node, end_node], fill=purple, width=2)  # Change fill and width as needed

        waypoints = []

        for current, parent_node in path:
            draw.line([current, parent_node], fill=(255, 0, 0, 255), width=2)
            waypoints.append(list(current))

        smoothed_path = [(round(x[0]), round(x[1])) for x in convert_to_coordinates(smooth_path(list(
            end), list(start), waypoints))]

        for coord in range(len(smoothed_path) - 1):
            draw.line([smoothed_path[coord], smoothed_path[coord + 1]], fill=blue, width=1)

    box = (start[0] - 3, start[1] - 3, start[0] + 3, start[1] + 3)
    draw.ellipse(box, outline="red", width=3)
    box = (end[0] - 3, end[1] - 3, end[0] + 3, end[1] + 3)
    draw.ellipse(box, outline="green", width=5)

    new_img.save(output_path)


def render_local_path_on_image(path, input_image, output_image):
    """
    Renders a local path on an input image and saves the output image.

    :param path: List of coordinates representing the local path.
    :type path: List[Tuple[int, int]]

    :param input_image: Path to the input image.
    :type input_image: str

    :param output_image: Path to save the output image.
    :type output_image: str
    """
    img = Image.open(input_image)
    draw = ImageDraw.Draw(img)

    for i in range(len(path) - 1):
        start = path[i][0], path[i][1]
        end = path[i+1][0], path[i+1][1]

        draw.line([start, end], fill=green, width=4)

    img.save(output_image)
