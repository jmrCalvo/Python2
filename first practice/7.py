#!/usr/bin/python3

def funcion_pedida(char_len,lista_cadenas):
    se_cumple=1
    for i in range(0,len(lista_cadenas)-1,1):
        for index in range(0,char_len,1):
            sub1=lista_cadenas[i][:char_len]
            if not lista_cadenas[i+1].endswith(sub1) :
                se_cumple=0
                break
    if se_cumple :
        print("se cumple el juego del telefono")
    else :
        print("NO se cumple el juego del telefono")

funcion_pedida(3,["nosep","sepdebe","ebesaleenlapelidulav","lavoratorioestamaldicho","chocolate"])
funcion_pedida(3,["osahfoihfs","sahbfiasjbf","isjfishf","saoifhishihaoihsifas","oafhbohbsibifbsijfb"])
