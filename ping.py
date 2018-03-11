#!/usr/bin/env python
# -*- coding: utf-8 -*-

'ping module'

__author__ = 'niubin'

import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse
resultX = []
resultY = []
Day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
filename = ''
def preprocessing(filename):
    fr = open(filename)
    lines = fr.readlines()
    for line in lines:
        if line[:3] == 'rtt':
            resultY.append(readDelay(line))
        if line[:3] in Day:
            data = line[:3]
            resultX.append(readTime(data, line))

    return resultX, resultY
import re

def readDelay(line):
    result = re.split(r'\s+|=|/',line)
    result = float(result[-4])
    return result #if result < 500 else 500
def readTime(data, line):
    #result = re.split(r'\s+|=|/', line)
    result = line.split(' ')
    time = result[-3]


    return data + ' ' + time


if __name__ == '__main__':

    if len(sys.argv) < 2 :
        print "filename is needed"
    else :
        filename = sys.argv[1]
    x, y = preprocessing(filename)
    print len(x)
    print len(y)
    fig, ax = plt.subplots()
    xticks = range(0,len(x),5000)
    xlabels = [x[index] for index in xticks]
    xticks.append(len(x))
    xlabels.append(x[-1])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation = 90)

    #x = np.arange(0,len(y) )

    print 'the len of data %d' % len(y)
    print 'the max of data %f' % max(y)
    print 'the min of data %f' % min(y)
    print 'the avg of data %f' % np.mean(y)
    print 'the std of data %f' % np.std(y)
    plt.plot(y)

    #plt.ylim((min(y),1000))
    plt.grid()
    plt.show()
