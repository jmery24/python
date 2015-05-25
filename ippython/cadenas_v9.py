# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 07:30:49 2013

@author: daniel
"""

#programa:cadenas_v9.py
#lee una cadena y verifica si alguna(s) palabra(s) tienen "num" caracteres
#se entra una cadena y un numero entero
#bucle <while> permite salir del programa con un espacio en blanco
#ejercicio 168 funciona ok

#data input
cadena = raw_input('Escribe una frase: ')
num = int(raw_input('Numero entero: '))

#processing
cadena = cadena + ' ' #agrego <blanco> final para completar calculo
while cadena != ' ':
    cantidad = 0    
    num_1 = 0

    for i in range(0,len(cadena)):  #calcula espacios en blanco
        cantidad +=1
        if cadena[i] == ' ' and cadena[i-1] == ' ':#no contar <blanco> inicial
            cantidad = 0
        if cadena[i] == ' ' and cadena[i-1] != ' ':
            if cantidad == num+1:
                num_1 += 1                
                cantidad = 0
            else:
                cantidad = 0
    if num_1 > 0:
        print 'si hay palabra(s) con %d caracteres.' %num
    else:
        print 'no hay palabra(s) con %d caracteres.' %num
    cadena = raw_input('Escribe una frase: ')
    if cadena == ' ':
        print 'gracias por utilizar el programa'
        break
    num = int(raw_input('Numero entero: '))
    cadena = cadena + ' ' #agrego <blanco> final para completar calculo