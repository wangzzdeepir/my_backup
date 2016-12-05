#!/usr/bin/python
"""This cell extracts features for both training and validation images, and 
store the extracted results in a .npy file.

"""
import os
import numpy as np

def getSeetaFeature(img_path):
    oStdout = os.popen('/home/deep/develop/SeetaFaceEngine-master/FaceIdentification/build/src/test/test_face_recognizer.bin'+' '+img_path)  
    vectorlist = []
    for line in oStdout.readlines():
        line = line.strip()
        if line.count(' ') == 2047:
            featlist = []
            featlist = line.split(' ', 2047)
            vectorlist.append(np.asarray(featlist).astype('float64'))
    return vectorlist

img_root = '/home/deep/develop/caffe/data/politics_project_data/data_11_16/images/'
extractedfeatures = np.zeros(shape = (1167, 2048))

for i in xrange(1000, 1167, 1):
    img_path = img_root + str(i + 1) + '.jpg'
    featurelist = getSeetaFeature(img_path)
    if len(featurelist) > 0:
        extractedfeatures[i, :] = featurelist[0]  #Assume there is only 1 face in the picture
    else:
        extractedfeatures[i, :] = -1
    print i + 1, '/1167'

np.save('data_11_16_extractedfeatures_1000_1167.npy', extractedfeatures)

print 'Done.'
