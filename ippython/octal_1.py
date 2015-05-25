# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 07:21:24 2013

@author: daniel
"""

#programa:octal_1.py
#programa que convierte una cadena [0,7] en numero octal
#ejercicio 185
#data input
octal = raw_input('<blanco> para salir o \nEscribe un numero octal: ')
if octal == ' ':#add
    print 'Gracias por utilizar el programa'#add

#processing
while octal != ' ':#add
    n = len(octal)
    valor = 0
    flag = 0
    for i in range(0,len(octal)):
        if octal[i] >= '0' and octal[i] < '8':
            valor = int(octal)
        else:
            flag +=1
    if flag > 0:
        print 'no es cadena octal'
    else:
        print ' Valor Octal es: %d ' %valor
    octal = raw_input('<blanco> para salir o \nEscribe un numero octal: ')#add
    if octal == ' ':
        print 'Gracias por utilizar el programa'#add
        break#add