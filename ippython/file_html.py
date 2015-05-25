# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 06:43:11 2013

@author: daniel
"""

# programa: files_html_xml.py
# el programa abre y muestra un fichero html o xml

try:
    nombre = raw_input('Nombre del file: ')
    fichero = open(nombre, 'r')
    for linea in fichero:
        print linea
    fichero.close()
except:
    print 'El file no existe'