# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:42:47 2013

@author: daniel
"""
#programa:cadenas_v8.py
#calcula la cantidad de palabras en base a los espacios en blanco
#y la longitud de la cadena determinada por un numero entero
#bucle <while> permite salir del programa con un espacio en blanco
#ejercicio 167

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
    print 'Palabras con %d caracteres: %d.' %(num, num_1)
    cadena = raw_input('Escribe una frase: ')
    if cadena == ' ':
        print 'gracias por utilizar el programa'
        break
    num = int(raw_input('Numero entero: '))
    cadena = cadena + ' ' #agrego <blanco> final para completar calculo