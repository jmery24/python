# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:00:13 2013

@author: daniel
"""

#programa:digitos.py
#lee una cadena y verifica si alguno(s) caracters(s) son digitos
#y calcula cuantos digitos hay en la cadena
#bucle <while> permite salir del programa con un espacio en blanco
#ejercicio 173 funciona ok

#data input
cadena = raw_input('Escribe una cadena: ')

#processing
cadena = cadena + ' ' #agrego <blanco> final para completar calculo
while cadena != ' ':
    digitos = 0
    for i in range(0,len(cadena)):#contador de caracteres
        if cadena[i] >= '0' and cadena[i] <= '9':#intervalo de digitos
            digitos += 1
            print cadena[i]
    print 'hay %d digitos en la cadena.' %digitos
    cadena = raw_input('Escribe una frase: ')
    if cadena == ' ':
        print 'gracias por utilizar el programa'
        break


