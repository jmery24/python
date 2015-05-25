# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:17:24 2013

@author: daniel
"""

#programa: numero_primo_v6.py
#variante del anterior programa numero_primo_v4 utilizando 
#un bucle <for in range> y <break>
# modulo math, carga modulo raiz cuadrada para la 3ra variante
from math import sqrt

#data input
num = int(raw_input('Introduce un numero entero: '))
creo_es_primo = True

#proccesing
#for divisor in range(2, num): #variante simple
#for divisor in range(2, n/2): #variante que funciona
for divisor in range(2, int(sqrt(num))): #variante que funciona
    if num % divisor == 0:
        creo_es_primo = False
        break
        
if creo_es_primo:
    print '%d es un numero primo' %num
else:
    print 'no es numero primo'
    print '%d / %d = %d' %(num, divisor, num/divisor)