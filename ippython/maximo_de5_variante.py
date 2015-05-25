# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 07:41:19 2013

@author: daniel
"""

#data input
a = int(raw_input('Elige un numero <A>: '))
b = int(raw_input('Elige un numero <B>: '))
c = int(raw_input('Elige un numero <C>: '))
d = int(raw_input('Elige un numero <D>: '))
e = int(raw_input('Elige un numero <E>: '))

#proccesing
candidato = a
if b > candidato:
    candidato = b
if c > candidato:
    candidato = c
if d > candidato:
    candidato = d
if e > candidato:
    candidato = e
maximo = candidato

#printout
print 'el maximo es ', maximo

    