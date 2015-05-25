# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 06:48:22 2013

@author: daniel
"""

# programa: files_tail_460.py
# el programa muestra las <n> ultimas filas de un archivo
# ejercicio 460

try:
    nombre = raw_input('Nombre del file: ')
    filas = int(raw_input('Cantidad de filas que muestra: '))
    fichero = open(nombre, 'r')
    lista = []
    for linea in fichero:
        if linea[-1] == '\n':
            linea = linea[:-1]
            lista.append(linea)
    filas = len(lista) - filas
    for i in range(filas, len(lista)):
        print i
        print lista[i]                
    fichero.close()
except:
    print 'El file no existe' 