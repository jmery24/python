# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 07:01:59 2013

@author: daniel
"""

#programa:binario_3.py
#programa que convierte numero binario en decimal, variante de binario_1 y 2
#data input
bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')

#processing
while bits != ' ':
    valor = 0
    for bit in bits:
        if bit == '1':
            valor += valor + 1
        else:
            valor += valor
    print 'Su valor decimal es: %d' %valor
    bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')
    if bits == ' ':
        print 'Gracias por utilizar el programa'
        break