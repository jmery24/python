# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 07:22:47 2013

@author: daniel
"""

#programa:encriptacion_2.py
#programa: encripta un texto, moviendo los caracteres y digitos <n> lugares 
#ejercicio 197, completo y funcionando
#data input
cadena = raw_input('Introduce una cadena: ')
n = int(raw_input('numero clave para la encriptacion: '))
encripta = ''
m = 26 - n#26 es la cantidad de caracteres del alfabeto
q = 10 - n#10 es la cantidad de digitos  

for i in range(0, len(cadena)):
    if cadena[i] == ' ':
        numero = ord(cadena[i])
        encripta = encripta + chr(numero)
    else:
        if cadena[i] >= 'a' and cadena[i] <= 'z':
            numero = ord(cadena[i]) + n
            if chr(numero) > 'z':
                numero = ord(cadena[i]) - m
                encripta = encripta + chr(numero)
            else:
#               numero = ord(cadena[i]) + n
                encripta = encripta + chr(numero)
        elif cadena[i] >= '0' and cadena[i] <= '9':
            numero = ord(cadena[i]) + n
            if chr(numero) > '9':
                numero = ord(cadena[i]) - q
                encripta = encripta + chr(numero)
            else:
#                numero = ord(cadena[i]) + n
                encripta = encripta + chr(numero)
        elif cadena[i] >= 'A' and cadena[i] <= 'Z':
            numero = ord(cadena[i]) + n 
            if chr(numero) > 'Z':
                numero = ord(cadena[i]) - m
                encripta = encripta + chr(numero)
            else:
#                numero = ord(cadena[i]) + n
                encripta = encripta + chr(numero)
        else:
            numero = ord(cadena[i])
            caracter = chr(numero)
            encripta = encripta + chr(numero)            
print encripta