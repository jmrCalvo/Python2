#!/usr/bin/python3

def buscar(cadena):
    busca="volwes"
    encontrado=0
    tamanio=0
    while (len(cadena)!=tamanio):
        posicion=cadena.find(busca,tamanio,len(cadena))
        if posicion!=-1 :
            encontrado=encontrado+1
            tamanio=tamanio+ posicion+len(busca)
        else:
            tamanio=len(cadena)
    return encontrado

print(buscar("volwesjidosbfaosfihsufab"))

print(buscar("volwesjidosbfaosfihsufabssoifsjfbspofvolwesobfdjbfidbfihjdbdvolwes"))

print(buscar(""))

print(buscar("aujsbgfijbasjfbiasbfjsbajbsibfajs"))
