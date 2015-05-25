# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:10:15 2013

@author: daniel
"""

# programa: files_teclado_repetido.py
# utilizacion del modulo <sys> y funcion <stdin>
# utiliza el teclado como un fichero mas. El bucle es infinito 
# parar: <control d> 

# importamos la funcion <stdin> del modulo <sys>
from sys import stdin

# programa
for linea in stdin:
    print linea