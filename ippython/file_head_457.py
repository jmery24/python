# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 05:50:53 2013

@author: daniel
"""

# programa: files_head_457.py
# el programa muestra las <n> primeras filas de un archivo
# ejercicio 457

try:
    nombre = raw_input('Nombre del file: ')
    filas = int(raw_input('Cantidad de filas que muestra: '))
    fichero = open(nombre, 'r')
    lista = []
    for linea in fichero:
        if linea[-1] == '\n':
            linea = linea[:-1]
            lista.append(linea)
    for i in range(0, filas):
        print i
        print lista[i]                
    fichero.close()
except:
    print 'El file no existe' 