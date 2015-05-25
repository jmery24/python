# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 07:33:50 2013

@author: daniel
"""

#programa:menu_elif_2.py
#calcula el diametro, area y perimetro a partir del valor del radio
#variante menu_elif_1

#modulo math
from math import pi

#data input
radio = float(raw_input('Valor del radio: '))
opcion = ' ' #inicializa opcion con una cadena vacia 

#computation and menu
print 'Menu de Opciones' 
while opcion != 'd':
    print 'a) Calcular el valor del diametro'
    print 'b) Calcular el valor del area'
    print 'c) Calcular el valor del perimetro'
    print 'd) Finalizar el programa'
    opcion = raw_input('Selecciona una opcion: ')
    if opcion == 'a' or opcion == 'a'.upper():
        diametro = 2 * radio
        print 'El valor del diametro es:  %2.4f' %diametro
    elif opcion == 'b' or opcion == 'b'.upper():
        area = pi * radio ** 2
        print 'el valor del area es:  %2.4f' %area
    elif opcion == 'c' or opcion == 'c'.upper():
        perimetro = 2 * pi * radio
        print 'El valor del perimetro es:  %2.4f' %perimetro
    elif opcion != 'd' or opcion == 'd'.upper():
        print 'Opciones: a b c d. Tu seleccionaste: ', opcion
    
print 'Gracias por usar el programa'