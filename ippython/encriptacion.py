# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 07:47:51 2013

@author: daniel
"""

#programa:encriptacion.py
#programa que encripta un texto, corriendo los caracteres <n> lugares
#ejercicio 197
#data input
cadena = raw_input('Introduce una cadena: ')
n = int(raw_input('numero clave para la encriptacion: '))
encripta = ''

for i in range(0, len(cadena)):
    if cadena[i] == ' ':
        numero = ord(cadena[i])
        encripta = encripta + chr(numero)
    elif cadena[i] != ' ':
        numero = ord(cadena[i]) + n
        caracter = chr(numero)
        encripta = encripta + chr(numero)
print encripta