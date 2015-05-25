# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:30:26 2013

@author: daniel
"""

# programa: file_linea_mas_larga_455
# el programa es una funcion que abre un <file> de texto y muestra la linea
# mas larga del file
# ejercicio 455

# funcion <linea_larga>
def linea_larga(fichero):
    lista = []
    for linea in fichero:
        if linea[-1] == '\n':
            linea = linea[:-1]
            lista.append(linea)
    return max(lista)
    
# abre el fichero y comprueba su existencia
try:
    nombre = raw_input('Nombre del file: ')
    fichero = open(nombre, 'r')
    print 'La linea mas larga es: ', linea_larga(fichero)
    fichero.close()
except:
    print 'El file no existe' 