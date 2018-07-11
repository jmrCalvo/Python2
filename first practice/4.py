#!/usr/bin/python3

def buscar(busca,cadena):

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

print(buscar("volwes","volwesjidosbfaosfihsufab"))

print(buscar("volwes","volwesjidosbfaosfihsufabssoifsjfbspofvolwesobfdjbfidbfihjdbdvolwes"))

print(buscar("volwes",""))

print(buscar("volwes","aujsbgfijbasjfbiasbfjsbajbsibfajs"))
