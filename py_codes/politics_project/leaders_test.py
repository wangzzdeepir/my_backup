#!/usr/bin/python
"""
"""
import numpy as np
import matplotlib.pyplot as plt

img = np.load('/home/deep/develop/caffe/data/leaders_images_augmentation/leaders_mean.npy')
img = img[img[[2, 1, 0], :, :]]
#plt.imshow(img)
print img.shape

