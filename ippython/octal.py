# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 06:48:08 2013

@author: daniel
"""

#programa:octal.py
#programa que convierte numero octal en decimal
#ejercicio 185
#data input
octal = raw_input('<blanco> para salir o \nEscribe un numero octal: ')
if octal == ' ':#add
    print 'Gracias por utilizar el programa'#add

#processing
while octal != ' ':#add
    n = len(octal)
    valor = 0
    for i in range(0,len(octal)):
        if octal[i] >= '0' or octal[i] < '8':
            valor = valor + int(octal[i]) * 8**(n-1)
        n -= 1
    print ' Su valor decimal es %d ' %valor
    octal = raw_input('<blanco> para salir o \nEscribe un numero octal: ')#add
    if octal == ' ':#add
        print 'Gracias por utilizar el programa'#add
        break#add
        