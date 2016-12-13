#!/usr/bin/python
"""This file generates lmdb file directly for non-image data.
"""
import numpy as np
import lmdb
import caffe


def data_to_lmdb(X, y, DST):
    """This function stores data X and corresponding label y into DST lmdb.
    """
    assert X.ndim == 4
    assert X.shape[0] == y.shape[0]
    N = X.shape[0]
    # ???
    X = X.astype('uint8')
    y = y.astype('int32')
    
    map_size = X.nbytes * 10
    env = lmdb.open(DST, map_size=map_size)

    with env.begin(write=True) as txn:
        for i in xrange(N):
            datum = caffe.proto.caffe_pb2.Datum()
            datum.channels = X.shape[1]
            datum.height = X.shape[2]
            datum.width = X.shape[3]
            #datum.data = X[i].tobytes()  # if numpy >= 1.9
            datum.data = X[i].tostring()  # if numpy < 1.9
            datum.label = int(y[i])
            str_id = '{:08}'.format(i)

            txn.put(str_id.encode('ascii'), datum.SerializeToString())





if __name__ == "__main__":
    N = 1000

    X = np.zeros((N,3,32,32), dtype = np.uint8)
    y = np.zeros(N, dtype=np.int64)

    map_size = X.nbytes * 10
    env = lmdb.open('mylmdb', map_size=map_size)

    with env.begin(write=True) as txn:
        #txn is a transaction object
        for i in range(N):
            datum = caffe.proto.caffe_pb2.Datum()
            datum.channels = X.shape[1]
            datum.height = X.shape[2]
            datum.width = X.shape[3]
            #datum.data = X[i].tobytes()  # if numpy >= 1.9
            datum.data = X[i].tostring()  # if numpy < 1.9
            datum.label = int(y[i])
            str_id = '{:08}'.format(i)

            txn.put(str_id.encode('ascii'), datum.SerializeToString())



