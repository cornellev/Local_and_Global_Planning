from PIL import Image, ImageDraw

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
            pixel_row[pixel] = 0 if pixel_row[pixel] == black else 1

    return pixels


def grid_to_image(grid, coordinate_pairs, output_path):
    height = len(grid)
    width = len(grid[0])

    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(new_img)
    start = (0, 0)
    end = (0, 0)

    for y in range(height):
        for x in range(width):
            new_img.putpixel((x, y), color_mapping.get(grid[y][x], black))
            if grid[y][x] == 3:
                start = (x, y)
            if grid[y][x] == 4:
                end = (x, y)

    for startq, endq in coordinate_pairs:
        draw.line([startq, endq], fill=purple, width=2)  # Change fill and width as needed

    box = (start[0] - 3, start[1] - 3, start[0] + 3, start[1] + 3)
    draw.ellipse(box, outline="red", width=3)
    box = (end[0] - 3, end[1] - 3, end[0] + 3, end[1] + 3)
    draw.ellipse(box, outline="green", width=5)

    new_img.save(output_path)

    new_img.save(output_path)
