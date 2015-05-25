# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 06:51:27 2013

@author: daniel
"""

#programa:binario_2.py
#programa que convierte numero binario en decimal, variante de binario_1
#data input
bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')

#processing
while bits != ' ':
    valor = 0
    for bit in bits:
        if bit == '1':
            valor = 2 * valor + 1
        else:
            valor = 2 * valor
    print 'Su valor decimal es: %d' %valor
    bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')
    if bits == ' ':
        print 'Gracias por utilizar el programa'
        break
