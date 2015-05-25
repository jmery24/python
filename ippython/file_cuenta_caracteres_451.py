# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 07:44:00 2013

@author: daniel
"""

# programa: file_cuenta_caracteres_451
# el programa abre un <file> y cuenta la cantidad de caracteres
# ejercicio 451

# abre el fichero y comprueba su existencia
try:
    nombre = raw_input('Nombre del file: ')
    print
    fichero = open(nombre, 'r')   
    cantidad = 0
    for linea in fichero:
        print linea
        cantidad = cantidad + len(linea)
    fichero.close()
    print 'Numero de caracteres: ', cantidad
except:
    print 'El file no existe'