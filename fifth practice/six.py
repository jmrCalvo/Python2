#!/usr/bin/python3
import os, sys
import re

#Write a function that, for a text given as a parameter, censures words that begin
#and end with voices. Censorship means replacing characters from odd positions with *.
def funcion(text,censura):
    textaux=text
    re.sub("\w^[voices]","*",textaux)
    re.sub("\w$[voices]","*",textaux)
    return text


t=sys.argv[1]
fd=open(t,"r")
s=fd.read()
s="myvoices me lo tiene que censurar y voicestu tambien en cambio voicemy no"
print(funcion(s,"voices"))
