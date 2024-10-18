from PIL import Image

if __name__ == '__main__':
    image_path_5 = 'images/in/img.png'
    image_5 = Image.open(image_path_5)

    image_5_rgba = image_5.convert("RGBA")

    pixels_5 = image_5_rgba.load()

    width_5, height_5 = image_5_rgba.size
    for y in range(height_5):
        for x in range(width_5):
            r, g, b, a = pixels_5[x, y]
            if r < 50 and g < 50 and b < 50:
                pixels_5[x, y] = (255, 255, 255, a)

    output_arrow_white_5 = 'images/out/new_one.png'
    image_5_rgba.save(output_arrow_white_5)
