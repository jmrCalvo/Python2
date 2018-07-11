#!/usr/bin/python3
import os
import sys

#Write a script that receives 3 parameters from the console. The first one will be a path to a file, the second a path to a directory and the third will be the size of a buffer. Script will copy the given file as a parameter into the given directory as a parameter, using a buffer of the third parameter size, in bytes.

nombre_archivo_definitivo=sys.argv[2]+"/"+sys.argv[1]
fdcreador=open(nombre_archivo_definitivo,mode="a")
value=int(sys.argv[3])
fdcreador.write(open(sys.argv[1],mode="r",buffering=value).read(value))


