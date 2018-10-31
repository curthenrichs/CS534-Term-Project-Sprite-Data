"""
Sorts images in a directory by their shape.

Usefull if a directory contains multiple sizes of images.
"""

import sys
import os

import matplotlib.image as mpimg
import numpy as np

import traceback

def sort_images(images):
    """ Sorts an image by its shape

    Images is a dictionary of {key : { 'img': np.array }} at input.
    For each image the shape is is used to compute a cluster id. This id is
    appended to the image sub-dictionary.
    """

    for imgName in images.keys():
        try:
            img = images[imgName]['img']
            shapeDirName = 'shape_' + str(img.shape[0]) + 'x' + str(img.shape[1]) + 'x' + str(img.shape[2])
            images[imgName]['cluster'] = shapeDirName
        except Exception as e:
            print(e)
            traceback.print_exc()
    return images

if __name__ == '__main__':

    # Get command-line args
    if len(sys.argv) != 3:
        print('{} sourceDirectory destinationDirectory'.format(sys.argv[0]))
        exit()
    else:
        sourceDirectory = sys.argv[1]
        destinationDirectory = sys.argv[2]

    # Get files in directory
    files = [f for f in os.listdir(sourceDirectory) if os.path.isfile(os.path.join(sourceDirectory,f))]

    # Open images and place into dictionary
    images = {}
    for f in files:
        images[f] = {}
        images[f]['img'] = mpimg.imread(os.path.join(sourceDirectory,f))

    # process images
    images = sort_images(images)

    # save images into directories based on cluster id
    for imgName in images.keys():
        try:
            shapeDirPath = os.path.join(destinationDirectory, images[imgName]['cluster'])

            if images[imgName] == 'shape_16x16x3':
                print(imageName)

            if not os.path.exists(shapeDirPath):
                os.makedirs(shapeDirPath)

            mpimg.imsave(os.path.join(shapeDirPath,imgName), images[imgName]['img'])
        except Exception as e:
            print(e)
            traceback.print_exc()
