#!/usr/bin/python3
def convertircadena(cadena):
    aux=cadena.upper()
    lista=aux.split(" ")
    solucion=""
    for elem in lista:
        solucion=solucion+elem+"_"
    return solucion

print(convertircadena("Federico Garcia Lorca fue uno de los mejores poetas de Granada y Espania"))
