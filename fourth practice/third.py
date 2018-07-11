#!/usr/bin/python3
import os
import sys

try:
    f=open(sys.argv[1],mode='a')
except:
    print("Unable to open file.txt")
try:    
    for keys,values in os.environ.items():
        f.write("{}\t{}\n".format(keys,values))
except:
    print("Unable to write")
