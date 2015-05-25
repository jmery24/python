# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:36:33 2013

@author: daniel
"""

#programa:digitos_1.py
#lee una cadena y verifica si alguno(s) caracters(s) son digitos
#y calcula cuantos numeros hay en la cadena
#bucle <while> permite salir del programa con un espacio en blanco
#ejercicio 174 - funciona: ok

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
            if cadena[i] >= '0' and cadena[i] <= '9' and cadena[i-1] >= '0' and cadena[i-1] <= '9':
                digitos -=1
    if digitos > 0:
        print 'hay %d numero(s) en la cadena.' %digitos
    else:
        print 'no hay numeros en la cadena'
    cadena = raw_input('Escribe una frase: ')
    cadena = cadena + ' '#agrego <blanco> final para completar calculo
    if cadena == ' ':
        print 'gracias por utilizar el programa'
        break
