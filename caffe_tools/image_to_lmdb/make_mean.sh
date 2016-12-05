#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

LMDB_PATH=$1
OUT_PATH=$2
TOOLS=$3

if [ -d "$OUT_PATH" ]; then
  echo "Error: $OUT_PATH already exits."
  exit 1
fi

$TOOLS/compute_image_mean $LMDB_PATH \
  $OUT_PATH

echo "Mean binaryproto created."
