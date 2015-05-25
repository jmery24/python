# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:07:55 2013

@author: daniel
"""

#programa:numero_primo_v2.py
#verifica si un numero dado es numero primo

#data input
num = int(raw_input('Introduce un numero entero: '))
creo_es_primo = True

#proccesing and printout
for divisor in range(2, num):
    if num % divisor == 0:
        creo_es_primo = False
        
if creo_es_primo:
    print 'el %d es un numero primo'%num
else:
    print 'el %d no es numero primo' %num
  