# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 07:10:59 2013

@author: daniel
"""

# programa: files_etc_passwd_461.py
# el programa muestra los usuarios en el sistema
# ejercicio 461

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
    for i in range(filas, filas + 1):
        print
        nombre = lista[i].split(':')
        print nombre[4]
    fichero.close()
except:
    print 'El file no existe'