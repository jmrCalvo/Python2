#!/usr/bin/python3
import os, sys
from stat import *
#Write a script that takes the following arguments:1 path,2 tree_depth,3 filesize,4 filecount,5 dircount and create a directory structure deep depth as follows: starting from the root path will be created dircount filecount directories and files containing filesize bytes (only the "a" character for example) and this process will be repeated recursively for each created directory until the desired depth is reached (no directories will be created in the directories at maximum adacity)
def crearcarpetas(patron,numero):
	nombre=patron+"/dir"
	for numer in range(0,numero,1):
		os.mkdir(os.path.join(patron,"dir%d"%numer))


def crearficheros(patron,numero,tamanio):
	nombre=patron+"/fil"

	for numer in range(0,numero,1):

		fd=open(os.path.join(patron,"fil%d"%numer),mode="a")
		s="a"*tamanio
		fd.write(s)
		fd.close()
def funcion(numero_carpetas1,numero_archivos1,path,profundidad1,tamanio_archivos1):
	print(path,profundidad1)
	profundidad=int(profundidad1)
	numero_carpetas=int(numero_carpetas1)
	numero_archivos=int(numero_archivos1)
	tamanio_archivos=int(tamanio_archivos1)
	if profundidad>=0:
		crearcarpetas(path,numero_carpetas)

		for directories in os.listdir(path):
				full_fileName =os.path.join(path,directories)
				funcion(numero_carpetas,numero_archivos,full_fileName,profundidad-1,tamanio_archivos)
	crearficheros(path,numero_archivos,tamanio_archivos)


funcion(sys.argv[5],sys.argv[4],sys.argv[1],sys.argv[2],sys.argv[3])
