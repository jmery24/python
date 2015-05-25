# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:57:41 2013

@author: daniel
"""

#programa:extension.py
#programa: solicita el nombre de un fichero y solo muestra su extension 
#ejercicio 195
#data input
cadena = raw_input('Nombre del fichero: ')
nueva_cadena = ''
flag = 0

for i in range(0, len(cadena)):
    if cadena[i] == '.':
        flag = 1        
    else:
        cadena = cadena
if flag == 0:
    print 'No es un fichero'
else:
    nueva_cadena = cadena[i - len(cadena)-2] + cadena[i - len(cadena)-1] + cadena[i - len(cadena)-0]
    print 'Nombre de la extension es: %s' %nueva_cadena
    