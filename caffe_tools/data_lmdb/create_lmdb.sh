#!/usr/bin/env sh
# Create the lmdb inputs
# N.B. set the path to the image data dirs
set -e

if [ -z "$6" ]; then
    echo usage: $0 OUT_PATH LIST_PATH TOOL_ROOT DATA_ROOT RESIZE_HEIGHT RESIZE_WIDTH
    exit
fi

OUT_PATH=$1
LIST_PATH=$2
TOOL_ROOT=$3
DATA_ROOT=$4
RESIZE_HEIGHT=$5
RESIZE_WIDTH=$6

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=$RESIZE_HEIGHT
  RESIZE_WIDTH=$RESIZE_WIDTH
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

echo $RESIZE_HEIGHT $RESIZE_WIDTH

if [ ! -d "$DATA_ROOT" ]; then
  echo "Error: DATA_ROOT is not a path to a directory: $DATA_ROOT"
  echo "Set the DATA_ROOT variable to the path" \
       "where the data is stored."
  exit 1
fi

if [ -d "$OUT_PATH" ]; then
  echo "Error: $OUT_PATH already exits."
  exit 1
fi

echo "Creating lmdb..."

GLOG_logtostderr=1 $TOOL_ROOT/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $DATA_ROOT \
    $LIST_PATH \
    $OUT_PATH


echo "lmdb created."
