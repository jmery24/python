# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:43:27 2013

@author: daniel
"""

#programa:digito.py
#escribe una cadena y detecta si hay digitos 

#data input
cadena = raw_input('Escribe una cadena: ')
digito = 0
numero = 0
#recorrido uno
for caracter in cadena:
    if caracter > '0' and caracter < '9':
        digito += 1
print '\nvariante uno'        
if digito > 0:
    print 'contiene digitos'
else:
    print 'no contiene digitos'

   
#variante dos, utiliza indexacion
for i in range(len(cadena)):
    if cadena[i] > '0' and cadena[i] < '9':
        numero += 1
print '\nvariante dos '
if numero > 0:
    print 'contiene digitos'
else:
    print 'no contiene digitos'
