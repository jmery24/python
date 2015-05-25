# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 07:50:26 2013

@author: daniel
"""

#data input
a = raw_input('Elige palabra <A>: ')
b = raw_input('Elige palabra <B>: ')
c = raw_input('Elige palabra <C>: ')
d = raw_input('Elige palabra <D>: ')
e = raw_input('Elige palabra <E>: ')

#proccesing
candidato = a
if b < candidato:
    candidato = b
if c < candidato:
    candidato = c
if d < candidato:
    candidato = d
if e < candidato:
    candidato = e
maximo = candidato

#printout
print 'la palabra menor es ', maximo
