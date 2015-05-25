# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 06:23:45 2013

@author: daniel
"""

#programa:potencia_v1.py
#introducir un numero y calcular la potencia del mismo en un rango de valores

#data input
num = int(raw_input('Introducir un numero entero: '))

#proccesing and printout
#utilizamos un contador for - in
for potencia in [2,3,4,5,6,7]:
    print 'el numero %d elevado a la potencia %d es igual a %d' %(num,potencia,num**potencia)

#variante del contador
for potencia in [2,3,4,5,6,7,8]:
    resultado = num ** potencia
    print 'el num %d elevado a %d es igual a %d' %(num, potencia,resultado)