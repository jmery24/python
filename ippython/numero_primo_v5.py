# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 08:04:42 2013

@author: daniel
"""

#programa:numero_primo_v5
#calcula todos los numeros primos comprendidos entre 1 el numero dado

#data input
limite = int(raw_input('Dame un numero: '))

#proccesing and printout
for num in range(2, limite+1):
    creo_es_primo = True
    for divisor in range(2,num):
        if num % divisor == 0:
            creo_es_primo = False
            break
    if creo_es_primo:
        print 'numero primo:', num