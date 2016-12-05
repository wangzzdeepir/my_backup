import os, sys
import numpy as np
import caffe
import cv2

caffe_root = '/home/deepir/facialscore/caffe-fast-rcnn/'
sys.path.insert(0, caffe_root + 'python')
os.chdir(caffe_root)

net_file = caffe_root + 'models/bvlc_alexnet/test.prototxt'
caffe_model = sys.path[0] + '/caffe_alexnet_train_iter_10000.caffemodel'
mean_file = sys.path[0] + '/ilsvrc_2012_mean.npy'

net = caffe.Net(net_file,caffe_model,caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data', 227) 
transformer.set_channel_swap('data', (2,1,0))

test = 0

if test == 1:
    equal = 0
    one = 0
    more = 0
    for line in open('test.txt','r').readlines():
        image = '/home/deepir/facialscore/data/yanzhi/faces/' + line.split()[0]
        im = caffe.io.load_image(image)
        img = cv2.imread(image)
        net.blobs['data'].data[...] = transformer.preprocess('data',im)
        out = net.forward()

        imagenet_labels_filename = '/home/deepir/facialscore/data/sysnet.txt'
        labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

        print net.blobs['prob'].data[0]
        top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
        for i in np.arange(top_k.size):
            print labels[top_k[i]]
        print line.split()[0]
        print (line.split()[1] + ' ' + labels[top_k[0]])
        truth = (int)(line.split()[1])
        prediction = (int)(labels[top_k[0]])
        img_path = '/home/deepir/facialscore/data/face/'
        if truth > 7:
            os.system('cp ' + image + ' ' + img_path + 'face_truth/8-9/')
        elif 5 < truth < 8:
            os.system('cp ' + image + ' ' + img_path + 'face_truth/6-7/')
        elif 3 < truth < 6:
            os.system('cp ' + image + ' ' + img_path + 'face_truth/4-5/')
        else:
            os.system('cp ' + image + ' ' + img_path + 'face_truth/0-3/')
        if prediction > 7:
            os.system('cp ' + image + ' ' + img_path + 'face_prediction/8-9/')
        elif prediction == 7:
            os.system('cp ' + image + ' ' + img_path + 'face_prediction/7/')
        elif prediction == 6:
            os.system('cp ' + image + ' ' + img_path + 'face_prediction/6/')
        elif 3 < prediction < 6:
            os.system('cp ' + image + ' ' + img_path + 'face_prediction/4-5/')
        else:
            os.system('cp ' + image + ' ' + img_path + 'face_prediction/0-3/')
        if truth == prediction:
            equal = equal + 1
        elif abs(truth - prediction) == 1:
            one = one + 1
        else:
            more = more + 1
    
    print equal #255
    print one #303
    print more #79

else:
    im = caffe.io.load_image('/home/deepir/facialscore/caffe-fast-rcnn/python/fan15.jpg')
    net.blobs['data'].data[...] = transformer.preprocess('data',im)
    out = net.forward()
    imagenet_labels_filename = '/home/deepir/facialscore/data/sysnet.txt'
    labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')
    
    print net.blobs['prob'].data[0]
    print type(net.blobs['prob'].data[0].flatten())
    print net.blobs['prob'].data[0].flatten().argsort()
    top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
    for i in np.arange(top_k.size):
        print labels[top_k[i]]
