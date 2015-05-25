# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:56:37 2013

@author: daniel
"""

#programa: subcadena_1.py
#ejercicio 199 y 200
#data input
cadena = raw_input('Escribe una cadena: ')
i = int(raw_input('Numero A: '))
j = int(raw_input('Numero B: '))
flag = 0

subcadena = ''

if i < 0:
    i = 0

if j > len(cadena):
    final = len(cadena)

if j < len(cadena):
    final = j
    
if i >= final:
    flag = 1

for k in range(i, final):
    subcadena += cadena[k]
if flag == 0:
    print 'Subcadena entre %i y %i es %s' %(i, final, subcadena)
else:
    print 'Subcadena en blanco'