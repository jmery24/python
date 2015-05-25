# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 07:57:41 2013

@author: daniel
"""

#programa: subcadena.py
#operador de corte
#data input
cadena = raw_input('Escribe una cadena: ')
i = int(raw_input('Numero A: '))
j = int(raw_input('Numero B: '))

if j > len(cadena):
    final = len(cadena)
else:
    final = j
subcadena = ''

for k in range(i, final):
    subcadena += cadena[k]
print 'Subcadena entre %i y %i es %s' %(i, final, subcadena) 
