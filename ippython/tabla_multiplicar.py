# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 06:43:51 2013

@author: daniel
"""

#programa:tabla_multiplicar.py
#introducir un numero y calcular la tabla de multiplicar del 1 al 10

#data input
num = int(raw_input('Introducir un numero entero: '))

#proccesing and printout
#utilizamos un contador for - in
for factor in [1,2,3,4,5,6,7,8,9,10]:
    print 'el numero %d multiplicado por %d es igual a %d' %(num,factor,num*factor)

#variante del contador
for factor in [1,2,3,4,5,6,7,8,9,10]:
    resultado = num * factor
    print 'el num %d multiplicado por %d es igual a %d' %(num, factor,resultado)
    
#variante del contador utilizando range
for factor in range(1,11):
    resultado = num * factor
    print 'el num %d multiplicado por %d es igual a %d' %(num, factor,resultado)