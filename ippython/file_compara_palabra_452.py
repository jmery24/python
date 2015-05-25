# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 08:06:21 2013

@author: daniel
"""

# programa: file_compara_palabra_452
# el programa abre un <file> de texto verifica si una <palabra> dada
# por teclado esta en el texto del <file> 
# ejercicio 452

# abre el fichero y comprueba su existencia
try:
    nombre = raw_input('Nombre del file: ')
    fichero = open(nombre, 'r')
    palabra = raw_input('Ingrese palabra: ')
    flag = 0
    for linea in fichero:
        if palabra in linea:
            flag += 1
        else:
            flag -= 1
    fichero.close()
    if flag > -3:
        print 'La palabra: %s, pertenece al texto' %palabra
    else:
        print 'La palabra: %s, no pertenece al texto' %palabra
except:
    print 'El file no existe'