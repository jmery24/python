# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:21:03 2013

@author: daniel
"""

def es_par(num):
    return num % 2 == 0
    
numero = int(raw_input('Escribe un numero: '))

print es_par(numero)
