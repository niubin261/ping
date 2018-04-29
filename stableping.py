#!/usr/bin/env python
# -*- coding: utf-8 -*-

'stableping module'

from __future__ import print_function
import sys
import signal
import time
import psutil
import re
import os
import subprocess


def start():
    pass
def get_pid(ip):
    cmd = "ps -aux "
    print("cmd = %s\n" % cmd)
    out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.readlines()
    print("out = %s\n" % out[1])
    print('l 10 = %s\n' %out[10])
    for l in out:


        if l.endswith('sudo python pingscript.py ' + ip + ' tesh.txt\n') is True:
            print("pidx = %s\n" % l)
            r = re.split("\s+",l)
            print("r = %s\n" % r)
            return int(r[1])

    return -1
def main(cnt):
    print('cnt = %d\n' % cnt)
    ip = 'youtube.com'
    if not subprocess.call(['ping', '-c', '1', ip]):
        cnt = 0

    else:
        pid = get_pid(ip)
        print("pid = %d\n" % pid)
        if pid != -1:
            os.kill(pid,signal.SIGKILL)
        time.sleep(10)
        cnt  = cnt + 1
        os.system('sudo python pingscript.py ' + ip + ' tesh.txt')
    return cnt
def quit(signal,framed):
    sys.exit()
if __name__ == '__main__':
    cnt = 0
    signal.signal(signal.SIGINT,quit)
    signal.signal(signal.SIGTERM,quit)
    while True:


            if main(cnt) > 3:
                exit()
