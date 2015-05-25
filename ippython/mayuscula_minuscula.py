# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 07:08:51 2013

@author: daniel
"""

#data input
letra = raw_input('escribe un caracter: ')

#proccesing
if ord(letra) >= 97 and ord(letra) <=122:
    print 'minuscula'
else:
    if ord(letra) >= 65 and ord(letra) <=90:
        print 'mayuscula'
    else:
        print 'otro caracter'