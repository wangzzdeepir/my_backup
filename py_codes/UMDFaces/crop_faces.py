#!/usr/bin/python
"""This cell crops images of UMDFaces using
the bounding box in .csv
"""
import csv
import cv2
from random import randint

CSV_SRC = '/home/deep/data/UMDFaces/umdfaces_batch1/umdfaces_batch1_ultraface.csv'
TXT = '/home/deep/data/UMDFaces/umdfaces_batch1/'
DST_DIR = '/home/deep/data/UMDFaces/batch1_cropped/images/'
DST_LIST = '/home/deep/data/UMDFaces/batch1_cropped/list.txt'

SCALE = 1.3
rand_seed = randint(0, 1000)

with open(CSV_SRC, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for i, line in enumerate(reader):
#         if i == rand_seed:
        if i % 2000 == 0:
            print i
        #if i > 30000:
        #    break
        if i >= 1:
            img_path = TXT + line[1]
            x = int(round(float(line[4])))
            y = int(round(float(line[5])))
            w = int(round(float(line[6])))
            h = int(round(float(line[7])))
            h, w = max(h,w), max(h,w)

            img = cv2.imread(img_path)
            new_x = x + int(w / 2) - (w / 2) * SCALE
            new_y = y + int(h / 2) - (h / 2) * SCALE - (h / 10) * SCALE
            cropped_img = img[new_y : new_y + SCALE * h, new_x : new_x + SCALE * w, :]
            if cropped_img.size >= 30*30*3:
                cropped_img = cv2.resize(cropped_img, (224, 224), interpolation = cv2.INTER_CUBIC)
                img_name = line[1].split('/')[1]
                status = cv2.imwrite(DST_DIR + img_name, cropped_img)
                with open(DST_LIST, 'a') as dst:
                    dst.write(img_path + ' ' + line[0] + '\n')
                
#                 print DST_DIR + img_name
#                 print i
#                 print status

print 'Done'
