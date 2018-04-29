#!/usr/bin/python
'''
calucate the rate of download video from bb qq ...
the method  is
pre : previous size of dir eg tmp/qq
now : now size of dir eg tmp/qq
rate : (now - pre) / 5
'''
import os
import time
def dirsize(path):
    size = 0
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            size = size + os.path.getsize(os.path.join(root,filename))
    return size

def cal(path,pre):
    now = dirsize(path)
    return now, (now - pre) / 5

if __name__ == '__main__':
    bbnow = 0
    qqnow = 0
    youkunow = 0
    iqiyinow = 0
    bbpath = os.path.join(os.getcwd(),"tmp/bb")
    qqpath = os.path.join(os.getcwd(),"tmp/qq")
    iqiyipath = os.path.join(os.getcwd(),"tmp/iqiyi")
    youkupath = os.path.join(os.getcwd(),"tmp/youku")
    f = open("./tmp/download.txt","a")
    try:

        while True:
            t = time.strftime('%m-%d-%H-%M-%S', time.localtime())
            bbnow, bbrate = cal(bbpath, bbnow)
            qqnow, qqrate = cal(qqpath, qqnow)
            youkunow, youkurate = cal(youkupath, youkunow)
            iqiyinow, iqiyirate = cal(iqiyipath, iqiyinow)
            f.write(t + "\n")
            f.write("bb:" + str(bbrate) + "\n")
            f.write("qq:" + str(qqrate) + "\n")
            f.write("youku:" + str(youkurate) + "\n")
            f.write("iqiyi:" + str(iqiyirate) + "\n")
            time.sleep(5)
    except:
        KeyboardInterrupt
    finally:


        f.close()



