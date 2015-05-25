# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:56:15 2013

@author: daniel
"""

# programa: lineas.py
# el programo abre un <file> y cuenta la cantidad de lineas

# abre el fichero y comprueba su existencia
try:
    nombre = raw_input('Nombre del file: ')
    fichero = open(nombre, 'r')
    contador = 0
    for linea in fichero:
        contador += 1
    fichero.close()
    print 'Numero de lineas: ', contador
except:
    print 'El file no existe'