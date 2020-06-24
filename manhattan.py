import numpy as np
from PIL import Image

# Distance Metric: Manhattan Distance
# Generate random images for test purposes.
# Find the distance betweeen two images, find a way to normalise them.

IMG_CHANNELS = 3
HORIZONTAL_RES = 1932
VERTICAL_RES = 2576
RGB_RANGE = 255


def manhattan_dist(v1, v2):
    step_one = np.divide(abs(v1 - v2), RGB_RANGE)  # Manhattan distance per channel, normalise using RGB range value.
    step_two = np.sum(step_one, axis=2) # Add all the distances per pixel
    step_three = np.divide(step_two, IMG_CHANNELS) # Normalise the distances using no. of channels
    step_four = np.sum(step_three, axis=None) # Add the normalised distance of all the pixels
    '''
    print('First transformation:')
    print(step_one)
    print('Second transformation:')
    print(step_two)
    print('Third transformation:')
    print(step_three)
    print('Fourth transformation:')
    print(step_four)
    '''
    result = np.divide(step_four, HORIZONTAL_RES*VERTICAL_RES) # Normalise the final distance using the resolution of the image.

    return result


# img_1 = np.random.randint(0, RGB_RANGE, (HORIZONTAL_RES, VERTICAL_RES, IMG_CHANNELS))
# img_2 = np.random.randint(0, RGB_RANGE, (HORIZONTAL_RES, VERTICAL_RES, IMG_CHANNELS))


# print(manhattan_dist(img_1, img_2))
images = ['IMG_6968.JPG', 'IMG_6969.JPG', 'IMG_6970.JPG', 'IMG_6971.JPG', 'IMG_6972.JPG', 'IMG_6974.JPG',
          'IMG_6975.JPG', 'IMG_6976.JPG']

for x in range(len(images)):
    img_1 = Image.open('.\\data\\{}'.format(images[x]))
    img_1.load()
    data_1 = np.asarray(img_1, dtype='int32')
    for y in range(x, len(images)):
        if y != x:
            img_2 = Image.open('.\\data\\{}'.format(images[y]))
            img_2.load()
            data_2 = np.asarray(img_2, dtype='int32')
            print('Manhattan distance between {} and {}: {}'.format(images[x], images[y], manhattan_dist(data_1, data_2)))
