#!/usr/bin/env python
import Queue
import os, sys
from threading import Thread
from subprocess import call

print sys.argv

src_dir = sys.argv[1]
dest_dir = sys.argv[2]
threads = sys.argv[3]

q = Queue.Queue()

subdirectories = os.listdir(src_dir)

for subdirectory in subdirectories:
    q.put(subdirectory)

def grab_data_from_queue():
    while not q.empty():
        sub_dir = q.get()
        call(['rsync', '-rpg', '%s/%s' % (src_dir, sub_dir), '%s' % dest_dir])
        print('done with %s' % sub_dir)
        q.task_done()

for i in range(int(threads)):
    t1 = Thread(target = grab_data_from_queue)
    t1.start()

q.join()
