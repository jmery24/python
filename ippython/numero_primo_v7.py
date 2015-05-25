# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:49:39 2013

@author: daniel
"""

#programa:numero_primo_v8.py
#obten los numeros primos en el intervalo (1, n)

#data input
limite = int(raw_input('Dame un numero: '))

primos = []

#proccesing and printout
for num in range(2, limite+1):
    creo_es_primo = True
    for divisor in range(2,num):
        if num % divisor == 0:
            creo_es_primo = False
            break
    if creo_es_primo:
        print 'numero primo:', num
        primos.append(num)
print 'lista de numeros primos: ', primos 