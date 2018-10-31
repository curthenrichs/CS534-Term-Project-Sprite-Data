"""
Generate a sample image of the first 9 sprites (or less) in a directory.

Used only for testing and documentation purposes.
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from os import listdir
from os.path import isfile, join

def plotGeneratedImages(images):
    """
    Generate an image that tiles first several sprites
    """

    fig = plt.figure(figsize=(9, 9))
    for i in range(9 if images.shape[0] > 9 else images.shape[0]):
        plt.subplot(3, 3, i+1)
        img = np.clip(images[i, :],0,1)
        img = img.reshape((32, 32, 4))
        plt.tight_layout()
        plt.imshow(img)
        plt.axis('off')
    return fig


if __name__ == "__main__":

    # Get command-line args
    if len(sys.argv) != 3:
        print('{} sourceFile destinationFile'.format(sys.argv[0]))
        exit()
    else:
        sourceDirectory = sys.argv[1]
        destinationFile = sys.argv[2]

    # get all files in directory,
    files = [f for f in listdir(sourceDirectory) if isfile(join(sourceDirectory, f))]

    # Read images into numpy array
    first = True
    for f in files:
        if not f == 'desktop.ini':
            raw = mpimg.imread(os.path.join(sourceDirectory,f))
            raw = np.reshape(raw,(1,raw.shape[0],raw.shape[1],raw.shape[2]))

            if first:
                first = False
                images = raw
            else:
                images = np.concatenate((images,raw), axis=0)

    # generate a titled image composed of first several sprites
    fig = plotGeneratedImages(images)
    fig.savefig(destinationFile)
