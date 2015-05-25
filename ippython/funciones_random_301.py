# -*- coding: utf-8 -*-
"""
Created on Sat May 25 07:52:25 2013

@author: daniel
"""

#programa: funciones_random_301.py
#funcion random tal que [0.0 <= x <= 10.0]]
#ejercicio 301

#importa funcion random
import random

#define funcion <aleatorio>
def aleatorio():
    numero = random.randint(1, 54) #numero aleatorio int 0 <= int < 6
#    numero = random.uniform(-10, 10) #numero aleatorio float 0.0 <= float < 10.0
    return numero

#cuerpo del programa
#activa la funcion
numero_aleatorio = aleatorio()
print numero_aleatorio    