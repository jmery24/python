# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 06:11:53 2013

@author: daniel
"""
#programa:binario_1.py
#programa que convierte numero binario en decimal
#data input
bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')

#processing
while bits != ' ':
    n = len(bits)
    valor = 0
    for bit in bits:
        if bit == '1':
            valor = valor + 2 ** (n-1)         
        n -= 1
    print 'Su valor decimal es: %d' %valor
    bits = raw_input('Espacio <blanco> para salir o \nEscribe un numero binario: ')
    if bits == ' ':
        print 'Gracias por utilizar el programa'
        break
