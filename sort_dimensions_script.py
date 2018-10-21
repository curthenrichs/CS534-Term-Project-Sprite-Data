
import sys
import os

import matplotlib.image as mpimg
import numpy as np

import traceback

def sort_images(images):

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

    if len(sys.argv) != 3:
        print('{} sourceDirectory destinationDirectory'.format(sys.argv[0]))
        exit()
    else:
        sourceDirectory = sys.argv[1]
        destinationDirectory = sys.argv[2]

    files = [f for f in os.listdir(sourceDirectory) if os.path.isfile(os.path.join(sourceDirectory,f))]

    images = {}
    for f in files:
        images[f] = {}
        images[f]['img'] = mpimg.imread(os.path.join(sourceDirectory,f))

    images = sort_images(images)

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
