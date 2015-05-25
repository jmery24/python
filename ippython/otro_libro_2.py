# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:41:57 2013

@author: daniel
"""

salir = False
while not salir:
    entrada = raw_input('> ')
    if entrada == 'adios':
        print 'Adios... gracias por usar este programa'
        salir = True
    else:
        print entrada
        