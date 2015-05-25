# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 05:19:52 2013

@author: daniel
"""

# programa: files_tabla_variante.py
# calcula el cuadrado de cada numero comprendido entre [1 5000]

# abre fichero
f = open('tabla.txt', 'w')

# calcula el cuadrado de los numeros en el intervalo [1 5000]
for i in range(1, 5001):
    f.write('%8d %8d\n' % (i, i ** 2))

# cierra fichero    
f.close()