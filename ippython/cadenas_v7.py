# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:22:48 2013

@author: daniel
"""

#programa:cadenas_v7.py
#calcula la cantidad de palabras en base a los espacios en blanco
#bucle <while> permite salir del programa con un espacio en blanco
#ejercicio 166

#data input
cadena = raw_input('Escribe una frase: ')

#processing
while cadena != ' ':
    cambio = 0    #inicializacion de variable
    for i in range(1,len(cadena)):  #calcula espacios en blanco
        if cadena[i] == ' ' and cadena[i-1] != ' ' :
            cambio = cambio + 1
    if cadena[-1] == ' ':
        cambio = cambio - 1 
    print 'Hay %d palabra(s) en la frase' % (cambio+1)
    cadena = raw_input('Escribe una frase: ')
print 'gracias por utilizar el programa'