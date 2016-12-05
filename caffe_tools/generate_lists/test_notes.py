#!/usr/bin/python
"""
"""
import generate_lists as gl

# SRC = '/home/deep/data/politics_projects/data_11_30/train.txt'
# BUF = '/home/deep/data/politics_projects/data_11_30/train2.txt'
# BUF2 = '/home/deep/data/politics_projects/data_11_30/train3.txt'
# DST = '/home/deep/data/politics_projects/data_11_30/train_list.txt'
# DST_14 = '/home/deep/data/politics_projects/data_11_30/train_14_list.txt'
# DST_BG = '/home/deep/data/politics_projects/data_11_30/train_bg_list.txt'
# TXT = '/home/deep/data/politics_projects/data_11_30/images/'
# TXT2 = '/home/deep/develop/caffe/data/politics_project_data/data_11_16/backgrounds/train/'
# DIR = '/home/deep/develop/caffe/data/politics_project_data/data_11_16/backgrounds/train/'

SRC = '/home/deep/data/politics_projects/data_11_30/validation.txt'
BUF = '/home/deep/data/politics_projects/data_11_30/validation2.txt'
BUF2 = '/home/deep/data/politics_projects/data_11_30/validation3.txt'
DST = '/home/deep/data/politics_projects/data_11_30/val_list.txt'
DST_14 = '/home/deep/data/politics_projects/data_11_30/val_14_list.txt'
DST_BG = '/home/deep/data/politics_projects/data_11_30/val_bg_list.txt'
TXT = '/home/deep/data/politics_projects/data_11_30/images/'
TXT2 = '/home/deep/develop/caffe/data/politics_project_data/data_11_16/backgrounds/validation/'
DIR = '/home/deep/develop/caffe/data/politics_project_data/data_11_16/backgrounds/validation/'

gl.merge_lines(SRC, BUF)
gl.prepend_txt(BUF, DST_14, TXT)
gl.annotate_dir(DIR, BUF2, 0)
gl.prepend_txt(BUF2, DST_BG, TXT2)
gl.concat_txt([DST_14, DST_BG], DST)

print 'Done!'