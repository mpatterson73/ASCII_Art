from PIL import Image
import numpy as np


def create_matrix(image):
    image.thumbnail((400, 600))
    # image.show()
    print(f'Thumbnail size: {image.size}')
    pixel_data = list(image.getdata())
    # for i in range(0, len(pixel_data), image.width):
    #    pixel_matrix = pixel_data[i:image.width]

    pixel_matrix = [pixel_data[i:i+image.width]
                    for i in range(0, len(pixel_data), image.width)]
    #print('Successfully constructed pixel matrix: ')
    #print(f'Pixel matrix size: {len(pixel_matrix[0])} x {len(pixel_matrix)}')
    return pixel_matrix


def convert_brightness(pixel_matrix):
    bright_matrix = []
    for i in range(len(pixel_matrix)):
        bright_matrix.append([round(sum(pixel)/len(pixel))
                              for pixel in pixel_matrix[i]])

    print("successfully created brightnenss matrix!")
    print(
        f'Brightness matrix size: {len(bright_matrix[0])} x {len(pixel_matrix)}')
    return bright_matrix


with open('Photos/grier_cat.jpeg', 'rb') as fp:
    img = Image.open(fp)

    print('Successfully loaded image!')
    print('Image Size: ', img.size)

    # print(list(img.getdata()))
    # print(pixel_array)
    print(convert_brightness(create_matrix(img)))
