#!/usr/bin/python3
import os, sys
import re


def p1(text):
    m=re.findall("(\w+)",text)
    return m
t=sys.argv[1]
fd=open(t,"r")
s=fd.read()
print(p1(s))
