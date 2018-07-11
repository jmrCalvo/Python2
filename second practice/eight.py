#!/usr/bin/python3
def coger(item,indices):
    if len(item)<=indices:
        return None
    else:
        return item[indices]


def separar(listas,indices):
    solucion=list()
    for item in listas:
        solucion.append(coger(item,indices))
    return solucion

def crear(listas,tama):
    solucion=list()
    for index in range(1,tama,1):
        solucion=solucion+separa(listas,index)
    for index in range(tama,len(listas),1):
        solucion.append(separa(listas,index))
    return solucion
