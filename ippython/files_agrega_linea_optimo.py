# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 07:23:59 2013

@author: daniel
"""

# programa: files_agrega_linea_optimo.py
# se agrega una linea o nota utilizando <a>

nota = raw_input('Linea para agregar: ')

f = open('texto.txt', 'a')
f.write(nota + '\n')
f.close()