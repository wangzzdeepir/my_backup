#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

EXAMPLE=./
DATA=./
TOOLS=/home/deep/develop/caffe/build/tools

DATA_ROOT=/

# Set RESIZE=true to resize the images to MxN. Leave as false if images have
# already been resized using another tool.
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=100
  RESIZE_WIDTH=100
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$DATA_ROOT" ]; then
  echo "Error: DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_lmdb.sh to the path" \
       "where the data is stored."
  exit 1
fi

echo "Creating lmdb..."
rm -rf $EXAMPLE/train_lmdb
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $DATA_ROOT \
    $DATA/datalist_train.txt \
    $EXAMPLE/train_lmdb

echo "Done."
