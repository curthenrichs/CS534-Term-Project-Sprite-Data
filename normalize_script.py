"""
Normalize the image to RGBA with provided pixel resolution

Note: padding and cropping could be more elegant. I did it quick and frankly it
works.
"""

import sys
import os
from os import listdir
from os.path import isfile, join

import matplotlib.image as mpimg
import numpy as np

import traceback

def enforce_RGBA_channels(img):
    """
    Convert an image to RGBA if possible.

    Cases supported:
        + Already in RGBA
        + In RGB
        + In Grayscale (single-channel)
    """

    if len(img.shape) < 3 or img.shape[2] < 4:
        if len(img.shape) == 2 or img.shape[2] == 1:
            # gray-scale to average RGB + full A
            alpha = np.ones((img.shape[0],img.shape[1],1))
            if len(img.shape) == 2:
                img = np.reshape(img,(img.shape[0],img.shape[1],1))
            img = np.concatenate((img,img,img,alpha), axis=2)
        elif len(img.shape) < 2 or img.shape[2] != 3:
            raise Exception('Image is not standard size')
        else:
            # RGB image
            alpha = np.ones((img.shape[0],img.shape[1],1))
            img = np.concatenate((img,alpha),axis=2)
    elif img.shape[2] > 4:
        raise Exception('Image is not standard size')
    return img

def crop_image_x(img, normX):
    """
    Crops image along X direction (balanced)
    """

    diff = img.shape[1] - normX
    startX = diff//2
    if diff % 2 != 0:
        startX += 1
    stopX = img.shape[1] - diff//2

    return img[:,startX:stopX]

def crop_image_y(img, normY):
    """
    Crops image along Y direction (balanced)
    """

    diff = img.shape[0] - normY
    startY = diff//2
    if diff % 2 != 0:
        startY += 1
    stopY = img.shape[0] - diff//2

    return img[startY:stopY,:]

def pad_image_x(img, normX):
    """
    Pads image along X direction (balanced)
    """

    diff = normX - img.shape[1]
    padWidth = diff//2

    padRightWidth = padWidth
    if diff % 2 != 0:
        padLeftWidth = padWidth+1
    else:
        padLeftWidth = padWidth

    return np.concatenate(
        (
            np.zeros((img.shape[0], padLeftWidth, img.shape[2])),
            img,
            np.zeros((img.shape[0], padRightWidth, img.shape[2]))
        ),
        axis=1
    )

def pad_image_y(img, normY):
    """
    Pads image along Y direction (balanced)
    """

    diff = normY - img.shape[0]
    padWidth = diff//2

    padBottomWidth = padWidth
    if diff % 2 != 0:
        padTopWidth = padWidth+1
    else:
        padTopWidth = padWidth

    return np.concatenate(
        (
            np.zeros((padTopWidth, img.shape[1], img.shape[2])),
            img,
            np.zeros((padBottomWidth, img.shape[1], img.shape[2]))
        ),
        axis=0
    )

def normalize_images(images, normX, normY):
    """
    process the images to fit new size
    if original size is greater than norm -> crop image by center
    if original size is less than norm -> padd image with zeros
    regardless enforce RGBA representation
    """

    for imgName in images.keys():
        try:
            img = images[imgName]['img']
            img = enforce_RGBA_channels(img)

            if img.shape[1] > normX: # crop
                img = crop_image_x(img,normX)
            elif img.shape[1] < normX: # pad
                img = pad_image_x(img,normX)

            if img.shape[0] > normY: # crop
                img = crop_image_y(img,normY)
            elif img.shape[0] < normY: # pad
                img = pad_image_y(img,normY)
            images[imgName]['img'] = img

        except Exception as e:
            print(e)
            traceback.print_exc()

    return images


if __name__ == '__main__':

    # Get command-line args
    if len(sys.argv) != 5:
        print('{} sourceDirectory destinationDirectory normX normY'.format(sys.argv[0]))
        exit()
    else:
        sourceDirectory = sys.argv[1]
        destinationDirectory = sys.argv[2]
        normX = int(sys.argv[3])
        normY = int(sys.argv[4])

    # get all files in directory,
    files = [f for f in listdir(sourceDirectory) if isfile(join(sourceDirectory, f))]

    # Open images and place into dictionary
    images = {}
    for f in files:
        if not f == 'desktop.ini':
            images[f] = {}
            images[f]['img'] = mpimg.imread(os.path.join(sourceDirectory,f))

    # process images
    images = normalize_images(images,normX,normY)

    # save images into directory
    for imgName in images.keys():
        try:
            mpimg.imsave(join(destinationDirectory,imgName), images[imgName]['img'])
        except Exception as e:
            print(e)
            traceback.print_exc()
