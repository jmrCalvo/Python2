#!/usr/bin/python3
import os, sys
import re


#Write a function that receives as a parameter a regex string,
# a text string and a whole number x, and returns those long-length
#x substrings that match the regular expression.
def funcion(regex,text,x):
    l=[]
    m=re.findall("(\w+)",text)
    for elem in m:
         result=re.search(regex,elem)
         if result:
            if len(elem)>=x:
                l.append(elem)
    return l
t=sys.argv[1]
fd=open(t,"r")
s=fd.read()
print(funcion("ado",s,10))
