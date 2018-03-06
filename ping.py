#!/usr/bin/env python
# -*- coding: utf-8 -*-

'ping module'

__author__ = 'niubin'

import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse
results = []

filename = './ping2'
def preprocessing(filename):
    fr = open(filename)
    lines = fr.readlines()
    for line in lines:
        if line[:3] == 'rtt':
            results.append(readDelay(line))

    return results
import re

def readDelay(line):
    result = re.split(r'\s+|=|/',line)
    result = float(result[-4])
    return result #if result < 500 else 500
def readTime(line):
    pass

if __name__ == '__main__':

    if len(sys.argv) < 2 :
        print "filename is needed"
    else :
        filename = sys.argv[1]
    y = preprocessing(filename)

    x = np.arange(0,len(y) )

    print 'the len of data %d' % len(y)
    print 'the max of data %f' % max(y)
    print 'the min of data %f' % min(y)
    print 'the avg of data %f' % np.mean(y)
    print 'the std of data %f' % np.std(y)
    plt.plot(x,y)
    plt.ylim((min(y),1000))

    plt.show()
