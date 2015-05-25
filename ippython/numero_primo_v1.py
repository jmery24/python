# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 07:41:01 2013

@author: daniel
"""

#programa:numero_primo_v1.py
#verifica si un numero dado es numero primo

#data input
num = int(raw_input('Introduce un numero entero: '))
restos_no_nulos = 0 #inicializa la variable en cero

#proccesing and printout
for divisor in range(2, num):
    if num % divisor != 0:
        restos_no_nulos += 1
        
if restos_no_nulos == num - 2:
    print 'el %d es un numero primo'%num
else:
    print 'el %d no es numero primo' %num
  