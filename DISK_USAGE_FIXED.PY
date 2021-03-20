#!/usr/bin/env python3

import shutil
import sys
def check_disk usage(disk, min absolute, min percent):
    "'Returns True if there is enough free disk space, false otherwise.""
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent free = 180 • du.free / du.total
    #Calculate howmany free gigabytes
    gigabytes_free = du.free / 2••30
    if percent_free < min_percent or gigabytes free < min absolute:
        return False
    return True
#chech forat least2 GB and 10% free
if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)
    
print('Everything ok")
sys.exit(0)

input()
