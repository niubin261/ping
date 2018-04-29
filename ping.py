#!/usr/bin/env python
# -*- coding: utf-8 -*-

'ping module'
from __future__ import division
__author__ = 'niubin'

import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse
import csv
Day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
filename = ''
s = 0.0
lc = []
def preprocessing(filename):
    resultX = []
    resultY = []
    resultx = []
    resulty = []
    cnt = 0
    fr = open(filename)
    lines = fr.readlines()
    print type(lines)
    ll = len(lines)
    for l in range(0,ll -1):
        liner = lines[l]
        lined = lines[l + 1]
        if liner[:3] == 'rtt' and lined[:3] in Day:
            if cnt == 5 :
                s = sum(resulty) / 5
                resultY.append(s)
                resultX.append(resultx[3])
                cnt = 0
                del resultx
                del resulty
                resultx = []
                resulty = []
            else :
                resulty.append(readDelay(liner))
                data = lined[:3]
                resultx.append(readTime(data,lined))
                cnt = cnt + 1
    return resultX, resultY
import re

def readDelay(line):
    result = re.split(r'\s+|=|/',line)
    result = float(result[8])
    return result
def readTime(data, line):
    result = line.split(' ')
    time = result[-3].split(':')

    time = str((int(time[0]) + 19 ) % 24) + ':' + time[1]
    return  time


if __name__ == '__main__':

    if len(sys.argv) < 2 :
        print "filename is needed"
    else :
        filename = sys.argv[1]
    csvfile = file(filename + '.csv','wb')
    writer = csv.writer(csvfile)
    writer.writerow(['rtt','time'])

    x, y = preprocessing(filename)
    print len(x)
    print len(y)
    for i in range(len(x)):
        writer.writerow([x[i],y[i]])
    csvfile.close()
    fig, ax = plt.subplots()
    xticks = range(0,len(x),200)
    xlabels = [x[index] for index in xticks]
    xticks.append(len(x))
    xlabels.append(x[-1])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation = 90)


    print 'the len of data %d' % len(y)
    print 'the max of data %f' % max(y)
    print 'the min of data %f' % min(y)
    print 'the avg of data %f' % np.mean(y)
    print 'the std of data %f' % np.std(y)
    plt.plot(y)

    plt.ylim((min(y),np.mean(y) + np.std(y) * 2))
    plt.grid()
    plt.show()
