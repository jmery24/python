# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:15:01 2013

@author: daniel
"""

salir = False
while not salir:
    entrada = raw_input('>')
    if entrada == 'adios':
        salir = True
        print 'Adios... y gracias por usar el programa'
    else:
        print entrada