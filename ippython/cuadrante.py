# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 07:04:08 2013

@author: daniel
"""

from math import ceil

grados = float(raw_input("dame un angulo -en grados-: "))

cuadrante = int(ceil(grados)%360)/90

if cuadrante == 0:
    print "primer cuadrante"
if cuadrante == 1:
    print "segundo cuadrante"
if cuadrante == 2:
    print "tercer cuadrante"
if cuadrante == 3:
    print "cuarto cuadrante"
    