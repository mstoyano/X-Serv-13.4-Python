#!/usr/bin/python

fd = open("/etc/passwd", "r")
lista = fd.readlines()
fd.close()

for usuario in lista:
    nombre = usuario.split(':')
    print nombre[0] + " utiliza " + nombre[-1],
	
