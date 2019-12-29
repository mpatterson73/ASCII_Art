from PIL import Image
import numpy as np

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def create_matrix(image):
    image.thumbnail((300, 400))
    # image.show()
    print(f'Thumbnail size: {image.size}')
    pixel_data = list(image.getdata())
    # convert to a grid format or 2D array
    pixel_matrix = [pixel_data[i:i+image.width]
                    for i in range(0, len(pixel_data), image.width)]
    #print('Successfully constructed pixel matrix: ')
    #print(f'Pixel matrix size: {len(pixel_matrix[0])} x {len(pixel_matrix)}')
    return pixel_matrix


def convert_brightness(pixel_matrix):
    bright_matrix = []
    for row in pixel_matrix:
        bright_row = []
        for pixel in row:
            bright_row.append(round(sum(pixel)/len(pixel)))
        # print(bright_row)
        bright_matrix.append(bright_row)
    print(bright_matrix)

    print("successfully created brightnenss matrix!")
    print(
        f'Brightness matrix size: {len(bright_row)} x {len(bright_matrix)} ')
    return bright_matrix


def covert_ascii(brightness_matrix):
    ascii_matrix = []

    return


with open('Photos/grier_cat.jpeg', 'rb') as fp:
    img = Image.open(fp)

    print('Successfully loaded image!')
    print('Image Size: ', img.size)

    # print(list(img.getdata()))
    # print(pixel_array)
    array = convert_brightness(create_matrix(img))
    print(array[0])
