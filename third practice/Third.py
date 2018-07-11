#!/usr/bin/python3

def compare(dic1,dic2):
    for i in dic1.values():
        if i not in dic2:
            return False
    for i in dic2.values():
        if i not in dic1:
            return False
    return True    

d1=dict()
d2=dict()

compare(d2,d1)
