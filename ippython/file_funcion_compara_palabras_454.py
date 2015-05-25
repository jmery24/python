# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 08:46:17 2013

@author: daniel
"""
# programa: file_funcion_compara_palabra_454
# el programa es una funcion que abre un <file> de texto verifica si una 
# <palabra> dada por teclado esta en el texto del <file> 
# ejercicio 454

# funcion <compara_palabra>
def compara_palabra(fichero, palabra):
    lista = []
    for linea in fichero:
        if palabra in linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
                lista.append(linea)
    return lista

# abre el fichero y comprueba su existencia
try:
    nombre = raw_input('Nombre del file: ')
    fichero = open(nombre, 'r')
    palabra = raw_input('Ingrese palabra: ')
    print compara_palabra(fichero, palabra)
    fichero.close()
except:
    print 'El file no existe' 