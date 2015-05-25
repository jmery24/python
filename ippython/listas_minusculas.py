# -*- coding: utf-8 -*-
"""
Created on Thu May  2 07:13:56 2013

@author: daniel
"""

#programa: listas_minusculas.py
#verifica si una letra es minuscula

#ejercicio 237
letra = raw_input('Escribe una letra: ')

if (len(letra) == 1 and 'a' <= letra <= 'z') or letra in ['ñ']:
    print letra, 'Es una letra minuscula'
else:
    print letra, 'No es una letra minuscula'

#metodo alternativo 
#ejercicio 238   
letra = raw_input('Escribe una letra: ')

if len(letra) == 1 and ('a' <= letra <= 'z' or letra in 'ñ'):
    print letra, 'Es una letra minuscula'
else:
    print letra, 'No es una letra minuscula'