# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 06:42:32 2013

@author: daniel
"""

# programa: file_argv.py
# este programa te permite dar el nombre del file y la cantidad de filas
# que muestra, desde el llamdo a "correr" el programa
# ejemplo: $ python file_argv.py nombre_del_file.txt 10
# NO FUNCIONA

# importa la funcion <argv> del modulo <sys> from sys import argv
from sys import argv

# input utilizando funcion <argv>
nombre = argv[1]
numero = int(argv[2])

# programa
f = open(nombre, 'r')
n = 0 
for linea in f:
    n += 1
    print linea.rstrip()
    if n == numero:
        break
f.close()