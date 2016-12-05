#!/usr/bin/python
"""This file contains several functions to pre-process
the data or generate data augmentation.
"""
import cv2
import numpy as np
from random import randint
from random import uniform

def flip(img):
    """
    """
    cv2.flip(img, 1, img)
    return img

def data_augmentation(inimg, rotation = 15, scale = 0.1, noise = 0.05, shift = 7, flip = True, blur = 0.1):
    """Generates augmentation of input images.
    """
    cols, rows = inimg.shape[0:2]
    
    #Shift transform
    M_shift = np.float32([[1,0,randint(-shift,shift)],[0,1,randint(-shift,shift)]])
    inimg = cv2.warpAffine(inimg, M_shift, (cols,rows))
    
    #Rotation and scale transform
    M_sclrot = cv2.getRotationMatrix2D((cols,rows),uniform(-rotation, rotation),uniform(1-scale, 1+scale))
    inimg = cv2.warpAffine(inimg,M_sclrot, (cols,rows))
    
    #Random GaussianBlur
    if randint(0,5) > 3:
        sigmaXY = 0 * randint(0, round(255 * blur))
        ksize = 2 * randint(0,round(cols / 20)) + 1
        inimg = cv2.GaussianBlur(inimg, (11, 11), sigmaXY, sigmaXY)
    
    #Random pepper&salt noise
    for i in xrange(int(round(noise * cols * rows * 3))):
        inimg[randint(0, cols - 1), randint(0, rows - 1), randint(0, 2)] = 255 * (i % 2)
    
    #Random flip
    if randint(0, 1)>0:
        cv2.flip(inimg, 1, inimg)
        
    return inimg
    
