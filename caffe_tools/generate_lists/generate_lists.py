#!/usr/bin/python
"""This file includes many tools for generating train_list.txt.
"""
import os
import sys
import csv

def prepend_txt(SRC_PATH, DST_PATH, TXT):
    """This function prepends the TXT to each line in SRC_PATH.
    The results are saved into DST_PATH.
    """
    with open(SRC_PATH) as src:
        for line in src:
            with open(DST_PATH, 'a') as dst:
                dst.write(TXT + line)


def merge_lines(SRC_PATH, DST_PATH):
    """This function merge every two lines, so that the file ID and
    label are made into the same line.
    """
    with open(SRC_PATH) as src:
        for line in src:
            line = line.strip()
            if line.find('.') >= 0:
                buf = line
            else:
                with open(DST_PATH, 'a') as dst:
                    dst.write(' '.join([buf, str(int(line))])+'\n')


def annotate_dir(DIR, DST_PATH, LABEL):
    """This function annotates all files in the DIR with LABEL and
    save the .txt file into the DST_PATH. e.g. XXX.jpg 3
    """
    for roots, dirs, fils in os.walk(DIR):
        if roots[-1] != '/':
            roots += '/'
        for fil in fils:
            with open(DST_PATH, 'a') as dst:
                dst.write(roots.split(DIR)[1]+fil+' '+str(LABEL)+'\n')


def concat_txt(TXTLIST, DST_PATH):
    """This function concatenates .txt files in TXTLIST and save results
    in the DST_PATH.
    """
    with open(DST_PATH, 'w') as dst:
        for txt in TXTLIST:
            with open(txt) as src:
                for line in src:
                    if line != '\n':
                        dst.write(line)

def csv_list(SRC_PATH, ID_COL, FILE_COL):
    """This function generates list txt from csv. (UMDFaces)
    """
    debug = 0
    # with csv.reader(file(SRC_PATH, 'rb')) as table:
    #     for line in table:
    #         print type(line)
    #         print line
    #         debug += 1
    #         if debug >= 100:
    #             break
    with open(SRC_PATH, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print line[ID_COL]
            print line[FILE_COL]
            print type(line)
            debug += 1
            if debug >= 100:
                break


def spilit_list(SRC_PATH, MOD):
    """This function spilits a full list with format [FULL_PATH][SPACE][LABEL]
    into the list_train.txt and list_val.txt
    """
    HEAD = SRC_PATH.split('.txt')[0]
    TRAIN_PATH = HEAD + '_train.txt'
    VAL_PATH = HEAD + '_val.txt'
    with open(SRC_PATH) as txt:
        for i, line in enumerate(txt):
            line = line.strip()
            if i % MOD > 0:
                with open(TRAIN_PATH,'a') as train_list:
                    train_list.write(line + '\n')
            else:
                with open(VAL_PATH,'a') as val_list:
                    val_list.write(line + '\n')


def start_0(SRC_PATH, DST_PATH):
    """This function converts the labels in a .txt file starting from 1 to 0.
    """
    with open(SRC_PATH) as src:
        for line in src:
            line = line.strip()
            path, label = line.split(' ')
            with open(DST_PATH, 'a') as dst:
                dst.write(path + ' ' + str(int(float(label) - 1)) + '\n')

