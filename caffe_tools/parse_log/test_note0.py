#!/usr/bin/python
import parse_log as pl
import matplotlib.pyplot as plt

with open('/home/wangzongzuo/Documents/vggface/loss_UMDb1_train.log3') as TXT:
    iters, loss = pl.loss_val(TXT)
iters = range(0, 2200, 200)
plt.plot(iters[1:], loss[1:], '*')
plt.xlabel('iterations')
plt.ylabel('accuracy')
plt.show()
