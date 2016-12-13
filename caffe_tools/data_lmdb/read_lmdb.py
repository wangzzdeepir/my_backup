#!/usr/bin/python
"""
"""
import caffe
import numpy as np
import lmdb
import matplotlib.pyplot as plt


def show_lmdb(LMDB):
    lmdb_env = lmdb.open(LMDB)
    lmdb_txn = lmdb_env.begin()
    lmdb_cursor = lmdb_txn.cursor()
    datum = caffe.proto.caffe_pb2.Datum()

    for key, value in lmdb_cursor:
        datum.ParseFromString(value)
        label = datum.label
        data = caffe.io.datum_to_array(datum)
        print type(data), data.shape
        print label
        plt.imshow(np.sum(data[3:6,:,:], axis = 0))
        plt.show()









if __name__ == '__main__':
    lmdb_env = lmdb.open('/home/deep/data/UMDFaces/batch1_cropped/val_lmdb')
    lmdb_txn = lmdb_env.begin()
    lmdb_cursor = lmdb_txn.cursor()
    datum = caffe.proto.caffe_pb2.Datum()

    for key, value in lmdb_cursor:
        datum.ParseFromString(value)
        label = datum.label
        data = caffe.io.datum_to_array(datum)
        print type(data), data.shape
        #for l, d in zip(label, data):
        #        print l, d
        test_data = np.sum(data, axis=0)
        print test_data.shape
        print 'label: ', label
        plt.imshow(test_data, cmap='gray')
        plt.show()
