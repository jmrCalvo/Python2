#!/usr/bin/python3

def hacerlistas(lista,delimeter,posicion):
    if posicion!=len(delimeter):
        for elem in lista:
            #print(elem)
            aux=elem.split(delimeter[posicion])

            lista=hacerlistas(aux,delimeter,posicion+1)+lista
            lista.remove(elem)
    return lista

def contar(cadena,delimitadores):
    posicion=0

    lista=cadena.split(delimitadores[posicion])
    listacompleta=hacerlistas(lista,delimitadores,posicion+1)
    lista_nueva=[]
    for i in listacompleta:
     if i not in lista_nueva:
         lista_nueva.append(i)

    return len(lista_nueva)



print(contar("Viva la segunda republica espanola; ante todo, como siempre, hay algo mejor? pues claro que no! socio",[", ","; ","? ","! ",". "," ","\*","\n"]))

print(contar("esto es solo una prueba, no hay nada mas. La vida es asi",[", ","; ","? ","! ",". "," ","\*","\n"]))
