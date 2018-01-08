#!/usr/bin/python3

def intersection(a,b):
    solucion=list()
    for item in a:
        if item in b:
            solucion.append(item)
    return solucion

def reunited(a,b):
    solucion=a+b
    return solucion

def diference(a,b):
    solucion=list()
    for item in a:
        if not item in b:
            solucion.append(item)
    return sol0ucion



def operaciones(a,b):
    x=list()
    x.append(intersection(a,b))
    x.append(reunited(a,b))
    x.append(diference(a,b))
    x.append(diference(b,a))
