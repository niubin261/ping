import os
import time
import fnmatch

def clean(dirname):
    workdir = os.getcwd()
    fullname = os.path.join(workdir,dirname)
    if os.path.exists(fullname):
        for videoname in os.listdir(fullname):
            print videoname
            if videoname.endswith("mp4") or videoname.endswith("flv"):
                if os.path.getsize(os.path.join(fullname,videoname)) > 1000 :
                    os.remove(os.path.join(fullname,videoname))
    else :
        print "dir not exits"
if __name__ == '__main__':
    try:
        while True:
            time.sleep(10*60)
            clean("./tmp/bb")
            clean("./tmp/qq")
            clean("./tmp/iqiyi")
            clean("./tmp/youku")
    except:
        KeyboardInterrupt

