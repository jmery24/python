# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:59:56 2013

@author: daniel
"""

#programa: subcadena_3.py
#operador de corte
#ejercicio 204
#data input
cadena = raw_input('Escribe una cadena: ')
subcadena = ''

for k in range(0, len(cadena)):
    subcadena += cadena[k]
    print subcadena 
