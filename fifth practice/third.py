#!/usr/bin/python3
import os, sys
import re



#Write a function that receives as a parameter a string of text characters and a
#list of regular expressions and returns a list of strings that match on at least
# one regular expression given as a parameter.
def comprobar(palabra,lista,index):
    if index >= len(lista):
        return False
    else:
        if re.match(palabra,lista[index]):
            return True
        else:
            return comprobar(palabra,lista,index+1)



def funcion(text,lista):
        l=[]
        m=re.findall("(\w+)",text)
        for elem in m:
            if comprobar(elem,lista,0):
                if elem not in l:
                    l.append(elem)
        return l


t=sys.argv[1]
fd=open(t,"r")
s=fd.read()
l=["sado","amado","barco","animal","ijo"]
print(funcion(s,l))
