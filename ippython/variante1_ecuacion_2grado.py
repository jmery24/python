# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 06:38:55 2013

@author: daniel
"""

from math import sqrt #sqrt calcula la raiz cuadrada

# data input
a = float(raw_input("Numero A: "))
b = float(raw_input("Numero B: "))
c = float(raw_input("Numero C: "))

# data computation and output data
if a == 0 and b == 0 and c == 0:
    print 'Infinitas soluciones'
else:
    if a == 0 and b == 0:
        print 'No tiene solucion'
    else:
        if a == 0:
            x = -c/b
            print 'Ecuacion lineal: x= %4.3f' %x
        else:
            if b**2-4*a*c >= 0:
                x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
                x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
                print 'Soluciones de la ecuacion: x1= %4.3f, x2= %4.3f' % (x1,x2)
            else:
                print 'raiz cuadrada de numero negativo es un numero complejo'