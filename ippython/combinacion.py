# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 05:34:56 2013

@author: daniel
"""

#programa: combinaciones.py
#calcula la combinaciones de <m> elementos de un conjunto de <n> elementos

#data input y condicion n >= m
n = 0
m = 1
while n < m:
    print '<n> debe ser mayor o igual a <m>'
    n = int(raw_input('numero de agrupamiento <n>: '))
    m = int(raw_input('cantidad de elementos del conjunto <m>: '))
    
#factorial m!
i = 1
factorial_m = 1
while i <= m:
    factorial_m *= i
    i += 1
#print factorial_m
    
#factorial n!
i = 1
factorial_n = 1
while i <= n:
    factorial_n *= i
    i += 1
#print factorial_n
    
#factorial (n-m)!
i = 1
factorial_nm = 1
while i <= (n-m):
    factorial_nm *= i
    i += 1
#print factorial_nm
    
#calculo combinatorio
c = factorial_n/(factorial_nm * factorial_m)
print 'la cantidad de combinaciones de %d elementos agrupados en %d es: %d' %(n, m, c)
 