# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 06:44:38 2013

@author: daniel
"""

#programa:encriptacion_1.py
#programa que encripta un texto, corriendo los caracteres <n> lugares 
#pero las letras mayusculas no se cambian
#ejercicio variante del 197
#data input
cadena = raw_input('Introduce una cadena: ')
n = int(raw_input('numero clave para la encriptacion: '))
encripta = ''

for i in range(0, len(cadena)):
    if cadena[i] == ' ':
        numero = ord(cadena[i])
        encripta = encripta + chr(numero)
    else:
        if cadena[i] >= 'a' and cadena[i] <= 'z':
            numero = ord(cadena[i]) + n
            encripta = encripta + chr(numero)
        else:
            numero = ord(cadena[i])
            encripta = encripta + chr(numero)            
print encripta