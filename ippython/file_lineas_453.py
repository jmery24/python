# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 08:30:54 2013

@author: daniel
"""

# programa: file_lineas_453.py
# el programa abre un <file> y numera cada linea al mostrarla
# ejercicio 453

# abre el fichero y comprueba su existencia
try:
    nombre = raw_input('Nombre del file: ')
    print
    fichero = open(nombre, 'r')
    contador = 0
    for linea in fichero:
        contador += 1
        print contador, ')',
        print linea
    fichero.close()
except:
    print 'El file no existe'