#!/usr/bin/python3

def crearlista(lista,k):
    solucion=list()
    for index in range(0,len(lista),1):
        if index!=k:
            solucion.append(lista[index])
    return solucion

def creador2(listas,punt):
    if punt=0:
        return listas
    else:
        solucion=list()
        for index in range(0,len(lista),1):
            for item in creador(listas[index]):
                if item not in solucion:
                    solucion=solucion+item
        creador2(solucion,punt-1)

def creador(lista):
    solucion=list()
    for index in range(0,len(lista),1):
        solucion.append(crearlista(lista,index))
    return solucion;

def mimain(lis,punt):
    solucion_parcial=creador(lis)
    punt=punt-1
    solucion_total=creador2(solucion_parcial,punt)
    return solucion_total

def combinaciones(lista,numero):
    punteros=len(lista)-numero
    if punteros==0:
        return lista
    else:
        return mimain(listas,punteros)

x={1,2,3,4,5}
print(combinaciones(x,4))
