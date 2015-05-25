# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 07:03:12 2013

@author: daniel
"""

# programa: files_agrega_linea.py
# agregar una nueva linea a un fichero
# abre fichero_original 'r' y fichero_copia 'w', copia <original> en <copia>
# cierra ambos ficheros
# abre fichero_original 'w' y fichero copia 'r', copia <copia> en <original>
# agrega nueva_linea al fichero_original
# cierra ambos ficheros

nombre_fichero = raw_input('Nombre file original: ')
nueva_linea = raw_input('Escribe nueva linea: ')
nombre_copia = nombre_fichero + '.copia'

# copiamos <original> en <copia>
f1 = open(nombre_fichero, 'r')
f2 = open(nombre_copia, 'w')
for linea in f1:
    f2.write(linea)
f2.close()
f1.close()

# agregamos linea
f1 = open(nombre_copia, 'r')
f2 = open(nombre_fichero, 'w')
for linea in f1:
    f2.write(linea)
f2.write(nueva_linea + '\n')
f2.close()
f1.close()