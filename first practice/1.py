#!/usr/bin/python3

def cuentas(numero1,numero2):
    mayor,menor=0,0
    multiplicacion=1
    if numero1>numero2:
        mayor=numero1
        menor=numero2
    else:
        mayor=numero2
        menor=numero1
    for index in range(1,menor,1):
        if numero1%index==0 and numero2%index==0:
            multiplicacion=multiplicacion*index
    return multiplicacion

def mcd(lista):
    index=2
    resultado=cuentas(lista[0],lista[1]);
    while(index!=len(lista)):
        resultado=cuentas(resultado,lista[index])
        index=index+1
    return resultado

print(mcd([100,28,50]))
