#!/usr/bin/python3
import sys
import os
try:
    if os.path.isfile(sys.argv[1]):
        fo = open(sys.argv[1], "r+")
        print(fo.read(4096))
    else:
        try:
            os.path.isdir(sys.argv[1])
            print(os.listdir(sys.argv[1]))
        except:
            print("it is not a file nor a folder")	
except:
    print("Invalid parameters")
