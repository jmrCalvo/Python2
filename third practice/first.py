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
    x=set()
    x.add(intersection(a,b))
    x.add(reunited(a,b))
    x.add(diference(a,b))
    x.add(diference(b,a))
