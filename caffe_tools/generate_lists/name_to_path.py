#!/usr/bin/python
"""This file converts list files (.txt) from the format:
"XXX.jpg label" to the [full path][space][label] format. 
e.g."/home/....../XXX.jpg label"

Inputs:
    SRC_LIST:
    DST_LIST:
    DIR_PATH:
"""
import os
import sys

if len(sys.argv) != 4:
    print 'usage:'
    print sys.argv[0] + ' SRC_LIST DST_LIST DIR_PATH'
    print 'Find more details in the document strings in ' + sys.argv[0]
    sys.exit()

SRC_LIST = sys.argv[1]
DST_LIST = sys.argv[2]
DIR_PATH = sys.argv[3]


