# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 09:24:47 2013

@author: daniel
"""

caracter = raw_input("teclee un caracter: ")

if caracter == "()":
    print "es un parentesis cerrado"
else:
    if caracter == ")":
        print "es un parentesis abierto tambien"
    else:
            if caracter == "(":
                print "es un parentesis abierto"
            else:
                print "es otro caracter"
    


