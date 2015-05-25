# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:26:11 2013

@author: daniel
"""

#programa: utiliza_modulo_matriz.py
#utiliza las funciones del modulo <matriz>

#invoca las funciones del modulo <matriz>
from matriz import *

#cuerpo del programa

#menu - procesamiento - output
opcion = ' '

while opcion != 'e':
    print
    print '   Menu de Opciones'
    print
    print 'a) Crear Matriz '
    print 'b) Dimension de la Matriz'
    print 'c) Suma de Matriz A y B'
    print 'd) Producto de Matriz A y B'
    print 'e) Salir del Programa'
    print
    opcion = raw_input('Selecciona una opcion: ')
    if opcion == 'a' or opcion == 'a'.upper():
        print
        fila_a = int(raw_input('Cantidad de Filas: '))
        columna_a = int(raw_input('Cantidad de Columnas: '))
        A = lee_matriz(fila_a, columna_a)
        print        
        fila_b = int(raw_input('Cantidad de Filas: '))
        columna_b = int(raw_input('Cantidad de Columnas: '))
        B = lee_matriz(fila_b, columna_b)        
    elif opcion == 'b' or opcion == 'b'.upper():
        print 'Dimension de la Matriz A: ', dimension(A)
        print 'Dimension de la Matriz B: ', dimension(B)        
    elif opcion == 'c' or opcion == 'c'.upper():
        print 'Matriz A + Matriz B: ', suma(A, B)
    elif opcion == 'd' or opcion == 'd'.upper():
        print 'Matriz A x Matriz B: ', multiplica(A, B)
    elif opcion != 'e' or opcion == 'e'.upper():
        print 'Opciones: a b c d e. Tu seleccionaste: ', opcion
print 'Gracias por usar el programa'