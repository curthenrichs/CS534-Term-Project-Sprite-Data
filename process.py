import os
import sys

import matplotlib.image as mpimg
import numpy as np

import extraction_script
import normalize_script
import sort_dimensions_script

if __name__ == '__main__':

    if len(sys.argv) != 7:
        print('{} sourceFile destinationDirectory spriteX spriteY normX normY'.format(sys.argv[0]))
        exit()
    else:
        sourceFile = sys.argv[1]
        destinationDirectory = sys.argv[2]
        spriteX = int(sys.argv[3])
        spriteY = int(sys.argv[4])
        normX = int(sys.argv[5])
        normY = int(sys.argv[6])

    img = mpimg.imread(sourceFile)

    images = extraction_script.extract_images(img, spriteX, spriteY)
    images = normalize_script.normalize_images(images,normX,normY)
    images = sort_dimensions_script.sort_images(images)

    for imgName in images.keys():
        try:
            shapeDirPath = os.path.join(destinationDirectory, images[imgName]['cluster'])

            if not os.path.exists(shapeDirPath):
                os.makedirs(shapeDirPath)

            mpimg.imsave(os.path.join(shapeDirPath,imgName), images[imgName]['img'])
        except:
            print(e)
