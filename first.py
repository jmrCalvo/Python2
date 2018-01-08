#!/usr/bin/python3
def fibonnaci(lista,n,tope):
    if n==tope:
        print(lista)
    else:
        #print(lista[n-1])
        #print(lista[n-2])
        lista.append(lista[-2]+lista[-1])
        fibonnaci(lista,n+1,tope)
milista=[0,1]

fibonnaci(milista,1,5)
