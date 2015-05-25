# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 08:11:32 2013

@author: daniel
"""

#programa:cadenas_v3.py
#ejercicio 161 escribir una cadena y verificar si contiene un 
#digito o no lo contine


#data input
cadena = raw_input('Escribe una cadena: ')

#inicializacion de variable
digitos = 0

#processing
#verifica si la cadena contiene o no un digito
for i in range(len(cadena)):
    if cadena[i] >= '0' and cadena[i] <= '9' :
        digitos +=1
if digitos > 0:
    print 'La cadena contiene digitos'
else:
    print 'La cadena no contiene digitos'
        
    