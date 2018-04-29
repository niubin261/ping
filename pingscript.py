#!/usr/bin/python

from __future__ import print_function
import time
import psutil
import subprocess
import sys
import os
def lines(result):
    cnt = 0
    for s in result:
      if s == '\n':
          cnt = cnt + 1
    return cnt

def ping(filename ,ip):

    ping = 'ping -c 4 ' + ip
    f = open(filename, 'a+')

    p = subprocess.Popen(ping,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
    )

    result = p.stdout.read()
    time = 'date'
    p  = subprocess.Popen(time,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True
                         )
    result = result + p.stdout.read()
    cnt = lines(result)
    print ("result size = %d" % cnt)

    if cnt < 6:
        raise Exception("bad ping the dst is unreachable or packet loss 100%")
    else :
        f.write(result)
    f.close()
def start(rescnt):
    ip = ""
    filename = ""
    if len(sys.argv) < 3:
        print("filename & hosts is needed for py")
        exit()
    else:
        ip = sys.argv[1]
        filename = sys.argv[2]

    if rescnt < 3:
        try:
            while True:
                ping(filename,ip)
        except Exception,e:
            KeyboardInterrupt
            print ("exception : " , e)
            time.sleep(60)
            rescnt = rescnt + 1
            start(rescnt)
        finally:
            print("end process")
start(0)
