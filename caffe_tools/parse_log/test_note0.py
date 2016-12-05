#!/usr/bin/python
import parse_log as pl

with open('./loss_train_val.log') as TXT:
    pl.loss_train(TXT)
