# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 07:03:31 2013

@author: daniel
"""

#data input
a = int(raw_input('Elige un numero <A>: '))
b = int(raw_input('Elige un numero <B>: '))
c = int(raw_input('Elige un numero <C>: '))
d = int(raw_input('Elige un numero <D>: '))
e = int(raw_input('Elige un numero <E>: '))

#proccesing
candidato = b
if abs(c-a) < abs(candidato-a):
    candidato = c
if abs(d-a) < abs(candidato-a):
    candidato = d
if abs(e-a) < abs(candidato-a):
    candidato = e

#printout
print "el numero; ", candidato, "es el mas cercano al numero: ", a
