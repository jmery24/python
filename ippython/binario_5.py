# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 06:12:03 2013

@author: daniel
"""

#programa:binario_5.py
#programa que convierte numero binario en decimal con filtro por introduccion
#de caracteres distintos de "1" o "0"
#ejercicio 184

#data input
bits = raw_input('<blanco> para salir o \nEscribe un numero binario: ')
if bits == ' ':
    print 'Gracias por utilizar el programa'

flag = 0#variable para control de caracter != '0' o '1'

#processing
while bits != ' ':
    valor = 0
    for bit in bits:
        if bit == '0' or bit == '1':
            valor += valor + int(bit)
        else:
            flag += 1#asume valor por caracter != '0' o '1'
    if flag == 0:
        print 'Su valor decimal es: %d' %valor
    else:
        print 'no es un numero binario'
    bits = raw_input('<blanco> para salir o \nEscribe un numero binario: ')
    if bits == ' ':
        print 'Gracias por utilizar el programa'
        break