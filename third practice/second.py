#!/usr/bin/python3

s="sssome ssstsring"
d=dict()
for c in s:
    if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1

print (d)
