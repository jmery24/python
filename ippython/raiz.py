# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:25:48 2013

@author: daniel
"""

#programa:raiz.py
#calcula la raiz de un numero dado para un rango de 2 a 100

#data input
num = float(raw_input('Numero: '))

#proccesing and printout
for n in range(2,101):
    print 'la raiz %3d de %2.2f es %2.2f: ' %(n, num, num**(1.0/n))
    