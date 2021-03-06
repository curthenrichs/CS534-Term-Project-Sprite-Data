"""
Package a directory of sprites into a numpy serialized file (.npy) and a label
array as another (.npy)
"""

import sys
import os
from os import listdir
from os.path import isfile, join, isdir

import matplotlib.image as mpimg
import numpy as np

import traceback

def store_n_label(srcDir,images,label,recCount):
    """
    Recursively read in all images and generate labels

    images is in format of { key: { 'img': np.array, 'dir': string, 'lbl': string }}
    labels are generated from the directory hierarchy, appended by '_'.
    """

    if recCount < 0:
        return images

    for f in listdir(srcDir):
        if isdir(join(srcDir,f)):
            images = store_n_label(join(srcDir,f),images,label + '_' + f,recCount - 1)
        elif isfile(join(srcDir,f)) and not f == 'desktop.ini':
            images[f] = {}
            images[f]['lbl'] = label
            images[f]['dir'] = srcDir
            origImg = mpimg.imread(join(srcDir,f))
            resImg = np.reshape(origImg, (1,) + origImg.shape)
            images[f]['img'] = resImg

    return images

def package(destFileName, images):
    """
    Given image dictionary and location, save numpy files
    """

    labelList = []

    first = True
    for key in images.keys():
        if first:
            print(images[key]['img'].shape)
            imgSet = images[key]['img']
            first = False
        else:
            imgSet = np.concatenate((imgSet,images[key]['img']),axis=0)

        labelList.append(images[key]['lbl'])

        print(join(images[key]['dir'],key))
        print(images[key]['lbl'])

    np.save(destFileName + '_image.npy',np.array(imgSet))
    np.save(destFileName + '_label.npy',np.array(labelList))

if __name__ == '__main__':

    # Get command-line args
    if len(sys.argv) != 5:
        print('{} sourceDirectory destinationFileName rootLabel recursiveLimit'.format(sys.argv[0]))
        exit()
    else:
        sourceDirectory = sys.argv[1]
        destinationFileName = sys.argv[2]
        rootLabel = sys.argv[3]
        recursiveLimit = int(sys.argv[4])

    # Save the images
    images = store_n_label(sourceDirectory,{},rootLabel,recursiveLimit)
    package(destinationFileName,images)
