# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 07:09:19 2013

@author: daniel
"""

#programa:menu_elif.py
#calcula el diametro, area y perimetro a partir del valor del radio

#modulo math
from math import pi

#data input
radio = float(raw_input('Valor del radio: '))

#menu de opciones
print 'Menu de opciones'
print 'a) Calcular el valor del diametro'
print 'b) Calcular el valor del area'
print 'c) Calcular el valor del perimetro'
opcion = raw_input('Elige una de las tres opciones <a, b, c>: ')

#proccesing and printout
if opcion == 'a' or opcion == 'a'.upper():
    diametro = 2 * radio
    print 'El valor del diametro es:  %2.4f' %diametro
elif opcion == 'b' or opcion == 'b'.upper():
    area = pi * radio ** 2
    print 'el valor del area es:  %2.4f' %area
elif opcion == 'c' or opcion == 'c'.upper():
    perimetro = 2 * pi * radio
    print 'El valor del perimetro es:  %2.4f' %perimetro
else:
    print 'la opcion <', opcion, '> no es valida'