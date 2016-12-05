#!/usr/bin/python
"""
"""

import cv2

LIST_PATH = './list_train_s0.txt'
def aug_list(img):
    return [img, img]

with open(LIST_PATH) as LIST:
    for line in LIST:
        line = line.strip()
        path = line.split(' ')[0]
        name = path.split('.')
        label = line.split(' ')[1]
        alist = aug_list(cv2.imread(path))
        for i in xrange(len(alist)):
            print name[0] + '_aug' + str(i) + '.' + name[1] + ' ' + label + '\n'

