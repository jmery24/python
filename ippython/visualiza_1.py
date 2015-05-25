# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 07:09:26 2013

@author: daniel
"""

# programa: visualiza_1.py
# abre file, lee e imprime datos, cierra el file
# comprueba la exsutencia del file

import os

if os.path.exists('ejemplo.txt'):
    fichero = open('ejemplo.txt', 'r')
    for linea in fichero:
        if linea[-1] == '\n':
            linea = linea[:-1]
        print linea
    fichero.close()
else:
    print 'El File NO existe'