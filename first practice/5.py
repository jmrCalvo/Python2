#!/usr/bin/python3

def caracteres_especiales(cadena):
    if cadena.find("\n",0,len(cadena))==-1 and cadena.find("\t",0,len(cadena))==-1 and cadena.find("\r",0,len(cadena))==-1 and cadena.find("\b",0,len(cadena))==-1 and cadena.find("\f",0,len(cadena))==-1 and cadena.find("\v",0,len(cadena))==-1:
        print("No hay caracteres especiales")
    else :
        print("hay caracteres especiales")

caracteres_especiales("dohaishidshoifshsaf\nsifguhfuhsff\rasdbgifusiufauihfa")
caracteres_especiales("ajsbfisabfjbajfsbiabfs")
caracteres_especiales("\n\b\r")
caracteres_especiales("")
