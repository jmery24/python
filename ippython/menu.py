# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 06:30:35 2013

@author: daniel
"""

#programa:menu.py
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
if opcion == 'a' or opcion == 'a'.upper(): #calcula el diametro
    diametro = 2 * radio
    print 'El valor del diametro es:  %2.4f' %diametro
else:
    if opcion == 'b' or opcion == 'b'.upper(): #calcula el area
        area = pi * radio ** 2
        print 'el valor del area es:  %2.4f' %area
    else:
        if opcion == 'c' or opcion == 'c'.upper(): #calcula el perimetro
            perimetro = 2 * pi * radio
            print 'El valor del perimetro es:  %2.4f' %perimetro
        else:
            print 'la opcion <', opcion, '> no es valida'
         
            

