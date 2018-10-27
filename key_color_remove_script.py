import os
import sys
import uuid
from os import listdir
from os.path import isfile, join

import matplotlib.image as mpimg
import numpy as np

import traceback

def enforce_RGBA_channels(img):
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

def normalize_key_color(images,keyR,keyG,keyB,keyA):

    target = np.array([keyR,keyG,keyB,keyA])
    normal = np.array([0,0,0,0])

    for imgName in images.keys():
        try:
            img = images[imgName]['img']
            img = enforce_RGBA_channels(img)

            for x in range(0,img.shape[1]):
                for y in range(0,img.shape[0]):
                    if np.array_equal(img[y,x,:],target):
                        img[y,x,:] = normal

            images[imgName]['img'] = img

        except Exception as e:
            print(e)
            traceback.print_exc()

    return images

if __name__ == "__main__":

    if len(sys.argv) != 7:
        print('{} sourceDirectory destinationDirectory keyR keyG keyB keyA'.format(sys.argv[0]))
        exit()
    else:
        sourceDirectory = sys.argv[1]
        destinationDirectory = sys.argv[2]
        keyR = int(sys.argv[3])
        keyG = int(sys.argv[4])
        keyB = int(sys.argv[5])
        keyA = int(sys.argv[6])

    # get all files in directory,
    files = [f for f in listdir(sourceDirectory) if isfile(join(sourceDirectory, f))]

    images = {}
    for f in files:
        images[f] = {}
        images[f]['img'] = mpimg.imread(os.path.join(sourceDirectory,f))

    images = normalize_key_color(images,keyR,keyG,keyB,keyA)

    for imgName in images.keys():
        try:
            mpimg.imsave(join(destinationDirectory,imgName), images[imgName]['img'])
        except Exception as e:
            print(e)
            traceback.print_exc()
