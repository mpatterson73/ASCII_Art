# Reprint an image using ASCII characters

from PIL import Image
import numpy as np


def create_matrix(image):
    image.thumbnail((1000, 200))
    # image.show()
    print(f'Thumbnail size: {image.size}')
    pixel_data = list(image.getdata())
    # convert to a grid format or 2D array
    pixel_matrix = [pixel_data[i:i+image.width]
                    for i in range(0, len(pixel_data), image.width)]
    return pixel_matrix


def convert_brightness(pixel_matrix):
    bright_matrix = []
    for row in pixel_matrix:
        new_bright_row = []
        for pixel in row:
            new_bright_row.append(round(sum(pixel)/len(pixel)))
        # print(bright_row)
        bright_matrix.append(new_bright_row)
    # print(bright_matrix)
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


def print_ascii(ascii_matrix):
    ascii_pic = []
    for row in ascii_matrix:
        ascii_row = [char+char+char for char in row]
        print(''.join(ascii_row))
    return


with open('Photos/grier_cat.jpeg', 'rb') as fp:
    img = Image.open(fp)
    #print('Successfully loaded image!')
    #print('Image Size: ', img.size)
    # print(list(img.getdata()))
    # print(pixel_array)
    bright_array = convert_brightness(create_matrix(img))
    ascii_array = convert_ascii(bright_array)
    print_ascii(ascii_array)
