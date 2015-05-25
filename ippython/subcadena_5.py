# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:41:33 2013

@author: daniel
"""

#programa: subcadena_5.py
#si cadena B es prefijo de cadena A
#operador de corte
#ejercicio 207. trabaja ok
#data input
cadena_a = raw_input('Escribe cadena A: ')
cadena_b = raw_input('Escribe cadena B: ')
flag = 0
subcadena = ''

for k in range(0, len(cadena_a)):
    subcadena = subcadena + cadena_a[k]
    if subcadena == cadena_b:
        flag = 1
if flag > 0:
    print 'cadena B es prefijo de cadena A'
else:
    print 'cadena B no es prefijo de cadena A'
    
        
