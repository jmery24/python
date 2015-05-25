# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:40:32 2013

@author: daniel
"""

#programa: subcadena_2.py
#subcadena: numero inicial (i) y avanza (j)
#ejercicio 201
#data input
cadena = raw_input('Escribe una cadena: ')
i = int(raw_input('Numero A: '))
j = int(raw_input('Numero B: '))
flag = 0
num = i + j

subcadena = ''

if i < 0:
    i = 0

if num > len(cadena):
    num = len(cadena)

if num < len(cadena):
    num = num
    
if i >= num:
    flag = 1



for k in range(i, num):
    subcadena += cadena[k]
if flag == 0:
    print 'Subcadena de %i hasta %i es %s' %(i, num, subcadena)
else:
    print 'Subcadena en blanco'