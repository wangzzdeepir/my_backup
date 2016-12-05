#!/usr/bin/python
"""
"""

import image_preprocessing as ip
import numpy as np
import cv2

SRC_LIST = './list_train_s0.txt'
DST_LIST = './list_train_aug.txt'

with open(SRC_LIST) as LIST:
    for line in LIST:
        line = line.strip()
        path = line.split(' ')[0]
        name = path.split('.')
        label = line.split(' ')[1]
        img = cv2.imread(path)
        alist = [img, ip.flip(img)]
        for i in xrange(len(alist)):
            aug_path = name[0] + '_aug' + str(i) + '.' + name[1]
            cv2.imwrite(aug_path, alist[i])
            with open(DST_LIST, 'a') as dst:
                dst.write(aug_path + ' ' + label + '\n')

print 'Done.'


