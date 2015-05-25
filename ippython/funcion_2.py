# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 07:50:18 2013

@author: daniel
"""

def varios(param1, param2, **otros):
    for i in otros.items():
        print i
        
varios(8, 'casa', hola = 5)

def variedad(param1, param2, *otro):
    for val in otro:
        print val

variedad(1, 2, 'tres')
variedad(1, 2, 'tres', 'cuatro')
variedad(1, 2, 3, 4, 5)
variedad(1, 2, 3, 4, 5, 6)