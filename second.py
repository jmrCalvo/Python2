#!/usr/bin/python3
def es_primo(numero):
    if numero==2 or numero==1:
        return True;
    else:
        aux=3**numero
        aux1=aux%numero
        aux2=3%numero
        if aux1==aux2:
            return True
        else:
            return False


def prime(lista):
    solucion=list()
    for item in lista:
        if es_primo(item)==True:
            solucion.append(item)

    return solucion


x={1,3,5,7,16,9,8,2,4}
print(prime(x))
