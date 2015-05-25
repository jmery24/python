# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 08:28:16 2013

@author: daniel
"""

numero = int(raw_input("introduzca un numero par entero: "))

if ((numero/2)%2) == 0:
    print "no es el doble de un numero impar"
else:
    print "es un numero impar multiplicado por 2"