# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 07:08:19 2013

@author: daniel
"""

#programa:binario_4.py
#programa que convierte numero binario en decimal, variante 1, 2 y 3
#data input
bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')

#processing
while bits != ' ':
    valor = 0
    for bit in bits:
            valor += valor + int(bit)
    print 'Su valor decimal es: %d' %valor
    bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')
    if bits == ' ':
        print 'Gracias por utilizar el programa'
        break