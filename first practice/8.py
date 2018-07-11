#!/usr/bin/python3
def submultpilo (numero,sub):
    if numero%sub==0 :
        return 1
else:
    return 0


def posibles(numer):
    negativo=0-numer
    solucion=[]
    for index in range(negativo,numer,1):
        if submultpilo(numer,index)==1:
            solucion.append(index)
    return solucion

def calculo(lista):



def resolver(cadena):
    lista=cadena.split("+")
    aux=lista][-1].split("*")
    if len(aux)==1 :
        aux1=aux.split("^")
        if len(aux1)==1:
            #ahora hemos sacado que el ultimo literal es un numero o x
            if aux1[0]=="x":
                #una solucion es x=0
            else:
