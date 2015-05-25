# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:00:14 2013

@author: daniel
"""

# programa: files_teclado.py
# utilizacion del modulo <sys> y funcion <stdin>
# utiliza el teclasdo como un fichero mas

# importamos la funcion <stdin> del modulo <sys>
from sys import stdin

# input
print 'Teclea un texto y pulsa enter'
linea = stdin.readline()

# output
print
print 'Linea escrita: ', linea