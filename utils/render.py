from PIL import Image, ImageDraw

from utils.spline import smooth_path, convert_to_coordinates

white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red = (255, 0, 0, 100)
purple = (83, 11, 120, 150)
purple2 = (106, 12, 153, 100)
green = (0, 255, 0, 100)
pink = (255, 192, 203, 100)

color_mapping = {
    0: black,
    1: white,
    3: black,
    4: black,
    5: black
}


def image_to_grid(path):
    img = Image.open(path)

    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    for pixel_row in pixels:
        for pixel in range(len(pixel_row)):
            if all([x > 150 for x in pixel_row[pixel]]):
                pixel_row[pixel] = 1
            else:
                pixel_row[pixel] = 0

    return pixels


def grid_to_image(grid, coordinate_pairs, output_path):
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

    for startq, endq in coordinate_pairs:
        draw.line([startq, endq], fill=purple, width=2)  # Change fill and width as needed

    box = (start[0] - 3, start[1] - 3, start[0] + 3, start[1] + 3)
    draw.ellipse(box, outline="red", width=3)
    box = (end[0] - 3, end[1] - 3, end[0] + 3, end[1] + 3)
    draw.ellipse(box, outline="green", width=5)

    new_img.save(output_path)

    new_img.save(output_path)

def render_path(grid, edges, coordinate_pairs, output_path):
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

    for startq, endq in coordinate_pairs:
        draw.line([startq, endq], fill=purple, width=2)  # Change fill and width as needed

    # start = (start[1], start[0])
    # end = (end[1], end[0])

    waypoints = []

    current = end
    while current != start:
        draw.line([current, edges[current]], fill=red, width=2)
        current = edges[current]
        waypoints.append(list(current))

    smoothed_path = [(round(x[0]), round(x[1])) for x in convert_to_coordinates(smooth_path(list(
        end), list(start), waypoints))]
    print(smoothed_path)

    for coord in range(len(smoothed_path[:-1])):
        draw.line([smoothed_path[coord], smoothed_path[coord + 1]], fill=green, width=2)



    box = (start[0] - 3, start[1] - 3, start[0] + 3, start[1] + 3)
    draw.ellipse(box, outline="red", width=3)
    box = (end[0] - 3, end[1] - 3, end[0] + 3, end[1] + 3)
    draw.ellipse(box, outline="green", width=5)

    new_img.save(output_path)

    new_img.save(output_path)
