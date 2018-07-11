#!/usr/bin/python3
import os
import sys


def funcion(patron,tab):
	tabuladores=" "
	for numer in range(0,tab,1):
		tabuladores="	"+tabuladores
	for elem in os.listdir(patron):		
		elem=patron+"/"+elem
		print(tabuladores+elem)
		if os.path.isdir(elem) is True:	
			funcion(elem,tab+1)

print(sys.argv[1])

funcion(sys.argv[1],1)


