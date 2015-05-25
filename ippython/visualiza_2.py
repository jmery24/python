# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 07:02:11 2013

@author: daniel
"""

# programa: visualiza_2.py
# abre file, lee e imprime datos, cierra el file
# realiza una excepcion sobre un error I/O

try:
    fichero = open('ejemplo.txt', 'r')
    for linea in fichero:
        if linea[-1] == '\n':
            linea = linea[:-1]
        print linea
    fichero.close()
except:
    print 'El File NO existe'