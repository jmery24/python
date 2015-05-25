# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:53:19 2013

@author: daniel
"""

#programa: subcadena_6.py
#si cadena B es subcadena de cadena A
#operador de corte
#ejercicio 208:  no funciona ok
#data input
cadena_a = raw_input('Escribe cadena A: ')
cadena_b = raw_input('Escribe cadena B: ')
flag = 0
subcadena = ''

for k in range(0, len(cadena_a)):
    subcadena = cadena_a[k]
    print subcadena
    if subcadena == cadena_b:
        print subcadena
        flag = 1
if flag > 0:
    print 'cadena B es subcadena de cadena A'
else:
    print 'cadena B no es subcadena de cadena A'