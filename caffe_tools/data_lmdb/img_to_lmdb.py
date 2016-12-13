#!/usr/bin/python
"""This file creates lmdb for given .jpg(s), computes and stores mean in a
.binaryproto. This file creates lmdb according to the image paths and labels
given in the list, and computes the mean pixel value of the resized image,
the created mean is stored in the same directory as lmdb in a .binaryproto
file.

Inputs:
    LIST_PATH: Full file path for 'xxx.txt', each line should have the following
        format [FULL_PATH][SPACE][LABEL]. e.g. /home/...../xxx.jpg 3
    LMDB_PATH: Full path for target directory. e.g. /home/..../train_lmdb
    RESIZE_H: e.g. 224
    RESIZE_W: e.g. 224
    TOOL_ROOT(optional): Will use default if not specified. The default can be
    set in line 30.
"""

import os
import sys

if len(sys.argv) < 5:
    print 'usage:'
    print sys.argv[0] + ' LIST_PATH LMDB_PATH, RESIZE_H, RESIZE_W, \
        TOOL_ROOT(optional)'
    print 'See more details in the document strings in ' + sys.argv[0]
    sys.exit()

# Default directory for /caffe/build/tools.
# Note that the end of path has no '/'.
DEFAULT_TOOL_ROOT = '~/develop/caffe/build/tools'

LIST_PATH = sys.argv[1]
LMDB_PATH = sys.argv[2]
RESIZE_H = sys.argv[3]
RESIZE_W = sys.argv[4]

OUT_PATH = LMDB_PATH + '/mean.binaryproto'  # Path for mean.binaryproto.

if len(sys.argv) > 5:
    TOOL_ROOT = sys.argv[5]
else:
    TOOL_ROOT = DEFAULT_TOOL_ROOT

def create_lmdb(list_path, lmdb_path, resize_h, resize_w, tool_root=TOOL_ROOT):
    """This function calls ./create_lmdb.sh shell to create lmdb files.
    """
    data_root = '/'
    creat_lmdb_command = ' '.join(('./create_lmdb.sh', lmdb_path, list_path, \
        tool_root, data_root, resize_h, resize_w))
    os.system(creat_lmdb_command)

def make_mean(lmdb_path, out_path, tool_root=TOOL_ROOT):
    """This function calls ./make_mean.sh to compute mean for the lmdb images.
    """
    make_mean_command = ' '.join(('./make_mean.sh', lmdb_path, out_path, \
        tool_root))
    os.system(make_mean_command)

create_lmdb(LIST_PATH, LMDB_PATH, RESIZE_H, RESIZE_W)
make_mean(LMDB_PATH, OUT_PATH, TOOL_ROOT)
