#!/usr/bin/python
"""
"""
import read_lmdb as rlmdb
import non_img_lmdb as nitl
import numpy as np
import cv2
import os
from pylab import *

p1 = '/home/deep/data/UMDFaces/batch1_cropped/images/bruce_rauner_0025.jpg'
p2 = '/home/deep/data/UMDFaces/batch1_cropped/images/bruce_rauner_0026.jpg'
p3 = '/home/deep/data/UMDFaces/batch1_cropped/images/bruce_rauner_0027.jpg'

DST = 'DELETE_lmdb'
if not os.path.exists(DST):
    data = np.zeros((3, 6, 224, 224))
    img1 = cv2.imread(p1)
    img2 = cv2.imread(p2)
    img3 = cv2.imread(p3)
    print img1.shape
    
    def swap(X):
        return np.swapaxes(np.swapaxes(X, 0, 2), 1, 2)
    
    data[0,0:3,:,:] = swap(img1)
    data[0,3:6,:,:] = swap(img2)
    data[1,0:3,:,:] = swap(img2)
    data[1,3:6,:,:] = swap(img3)
    data[2,0:3,:,:] = swap(img1)
    data[2,3:6,:,:] = swap(img3)
    label = np.array([12,5,9])
    imshow(img1[:,:,[2,1,0]])
    show()
    nitl.data_to_lmdb(data, label, DST)

else:
    print 'lmdb found.'
    rlmdb.show_lmdb(DST)

print 'Done'

