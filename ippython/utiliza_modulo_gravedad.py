# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:22:13 2013

@author: daniel
"""

#programa: utiliza_modulo_gravedad.py
#utiliza las funciones y constantes en el modulo gravedad

from gravedad import *

#programa

#define funcion <menu>
def menu():
    opcion = ''
    while not ('a' <= opcion <= 'd'):
        print 'Fisica Gravitatoria'
        print 'a) Calcula Fuerza Gravitatoria'
        print 'b) Calcula Distancia'
        print 'c) Calcula Velocidad de Escape'
        print 'd) Salida del programa'
        opcion = raw_input('Escoja una opcion: ')
        if not (opcion >= 'a' and opcion <= 'd'):
            print 'Elija opciones validas (a b c d)'
    return opcion
    
#cuerpo del programa
#activa funcion <menu>
eleccion = menu()
if eleccion == 'a':
    print
    masa1 = float(raw_input('Masa del cuerpo A: '))
    masa2 = float(raw_input('Masa del cuerpo B: '))
    distancia = float(raw_input('Distancia entre ellos: '))
    print 'La Fuerza de Atraccion entre los dos cuerpos es: ', fuerza_grav(masa1, masa2, distancia) 
elif eleccion == 'b':
    print
    masa1 = float(raw_input('Masa del cuerpo A: '))
    masa2 = float(raw_input('Masa del cuerpo B: '))
    F = float(raw_input('Fuerza de Atraccion: '))
    print 'La distancia entre los dos cuerpos es: ', distancia(masa1, masa2, F)
elif eleccion == 'c':
    print 
    masa = float(raw_input('Masa del cuerpo: '))
    radio = float(raw_input('Radio del cuerpo: '))
    print 'La velocidad de Escape es: ', velocidad_escape(masa, radio)
elif eleccion == 'd':
    print
    print 'Gracias por utilizar el programa'
else:
    print
    print 'opcion no valida'




