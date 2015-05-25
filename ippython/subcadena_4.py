# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:12:29 2013

@author: daniel
"""

#programa: subcadena_4.py
#operador de corte
#ejercicio 205-206: no funciona bien
#data input
cadena = raw_input('Escribe una cadena: ')
num = int(raw_input('Cantidad de caracteres por subcadena: '))
num_1 = ((len(cadena) - num) / 2)#calcula la cantidad de subcadenas
print num_1
subcadena = ''

for k in range(0, len(cadena)):
    subcadena = subcadena + cadena[k]
for i in range(0,num_1):
    print subcadena[i]
    print subcadena[i:num+i]

