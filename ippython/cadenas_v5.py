# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 06:24:49 2013

@author: daniel
"""

#programa:cadenas_v5.py
#calcula la cantidad de palabras en base a los espacios en blanco
#bucle <while> permite salir del programa con un espacio en blanco
#de <blanco> a <no blanco>

#data input
cadena = raw_input('Escribe una frase: ')

#processing
while cadena != ' ':
    cambio = 0    #inicializacion de variable
    anterior = ' '  #inicializacion de variable
    for i in cadena:  #calcula espacios en blanco en la cadena
        if i == ' ' and anterior != ' ' :
            cambio +=1
        anterior = i
    if cadena[-1] == ' ':
        cambio -= 1 
    print 'Hay %d palabra(s) en la frase' % (cambio+1)
    cadena = raw_input('Escribe una frase: ')
print 'gracias por utilizar el programa'