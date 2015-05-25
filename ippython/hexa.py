# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 07:36:22 2013

@author: daniel
"""

#programa:hexa.py
#programa que convierte una cadena [0,9,A-F] en numero hexadecimal
#ejercicio 186
#data input
hexa = raw_input('<blanco> para salir o \nEscribe un numero hexa: ')
if hexa == ' ':
    print 'Gracias por utilizar el programa'

#processing
while hexa != ' ':
    n = len(hexa)
    valor = 0
    flag = 0
    for i in range(0,len(hexa)):
        if hexa[i] >= '0' and hexa[i] < '8' or hexa[i] >= 'A' and hexa[i] < 'G':
            valor = hexa
        else:
            flag +=1
    if flag > 0:
        print 'no es cadena hexa'
    else:
        print ' Valor Hexa es: ', valor
    hexa = raw_input('<blanco> para salir o \nEscribe un numero hexa: ')
    if hexa == ' ':
        print 'Gracias por utilizar el programa'
        break