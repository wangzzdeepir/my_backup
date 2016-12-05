#!/usr/bin/python

import numpy as np


def loss_train(TXT):
    for line in TXT:
        line = line.strip()
        if line.find('solver') >= 0:
            print line
