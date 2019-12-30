from PIL import Image
import numpy as np


def create_matrix(image):
    image.thumbnail((300, 400))
    # image.show()
    print(f'Thumbnail size: {image.size}')
    pixel_data = list(image.getdata())
    # convert to a grid format or 2D array
    pixel_matrix = [pixel_data[i:i+image.width]
                    for i in range(0, len(pixel_data), image.width)]
    # print('Successfully constructed pixel matrix: ')
    # print(f'Pixel matrix size: {len(pixel_matrix[0])} x {len(pixel_matrix)}')
    return pixel_matrix


def convert_brightness(pixel_matrix):
    bright_matrix = []
    for row in pixel_matrix:
        new_bright_row = []
        for pixel in row:
            new_bright_row.append(round(sum(pixel)/len(pixel)))
        # print(bright_row)
        bright_matrix.append(new_bright_row)
    print(bright_matrix)

    print("successfully created brightnenss matrix!")
    # print(
    # f'Brightness matrix size: {len(bright_row)} x {len(bright_matrix)} ')
    return bright_matrix


def convert_ascii(brightness_matrix):
    ascii_matrix = []
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for row in brightness_matrix:
        new_ascii_row = []
        for bval in row:
            new_ascii_row.append(
                ascii_chars[int(bval/255 * len(ascii_chars)) - 1])
        ascii_matrix.append(new_ascii_row)
    return ascii_matrix


with open('Photos/grier_cat.jpeg', 'rb') as fp:
    img = Image.open(fp)

    print('Successfully loaded image!')
    print('Image Size: ', img.size)

    # print(list(img.getdata()))
    # print(pixel_array)
    array = convert_brightness(create_matrix(img))

    print(convert_ascii(array)[0])
