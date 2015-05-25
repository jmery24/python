# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 05:12:43 2013

@author: daniel
"""

# programa: files_tabla.py
# calcula el cuadrado de cada numero comprendido entre [1 5000]

# abre fichero
f = open('tabla.txt', 'w')

# calcula el cuadrado de los numeros en el intervalo [1 5000]
for i in range(1, 5001):
    f.write(str(i) + ' ' + str(i ** 2) + '\n')

# cierra fichero    
f.close()