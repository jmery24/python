# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:16:18 2013

@author: daniel
"""

#programa: utiliza_modulo_minmax.py

from minmax import minimo, maximo

#cuerpo del programa

#input
numero_a = int(raw_input('Escriba un numero: '))
numero_b = int(raw_input('Escriba un numero: '))

#activa las funciones y output
print 'Numero minimo: ', minimo(numero_a, numero_b)
print 'Numero maximo: ', maximo(numero_a, numero_b)