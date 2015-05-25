# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 06:52:34 2013

@author: daniel
"""

# programa: visualiza.py
# abre un file, imprime los datos, cierra el file

# abrir file
fichero = open('ejemplo.txt', 'r')

# lee e imprime los datos
for linea in fichero:
    print linea
    
# cerrar file
fichero.close()