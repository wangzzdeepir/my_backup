#!/usr/bin/python

import numpy as np

def slice(IN, START, END):
    id1 = IN.find(START)
    id2 = IN.find(END, id1)
    return IN[id1 + len(START) : id2]

def loss_train(TXT):
    iters = []
    loss = []
    for line in TXT:
        if line.find('Iteration') >= 0 and line.find('loss') >= 0:
            iters.append(int(slice(line, 'Iteration ', ',')))
            loss.append(float(slice(line, ', loss = ', 'UNMATCHEDSTRING')))
    return iters, loss

def loss_val(TXT):
    iters = []
    acc = []
    for line in TXT:
        if line.find('Test') >= 0 and line.find('accuracy') >= 0:
            print line
            #iters.append(int(slice(line, 'Iteration ', ',')))
            print slice(line, 'accuracy = ', 'UNMATCHEDSTRING')
            acc.append(float(slice(line, 'accuracy = ', 'UNMATCHEDSTRING')))
    return iters, acc
