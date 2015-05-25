# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 07:59:32 2013

@author: daniel
"""

#programa:mcd.py
#calcular el maximo comun divisor (MCD) de dos numeros enteros

#data input
num1 = int(raw_input('primer numero: '))
num2 = int(raw_input('segundo numero: '))

#computation
if num2 > num1: #para que sea indistinto que numero es mayor
    resto = num2 % num1
else:
    resto = num1 % num2
    
if resto != 0:
    resultado = num2 % resto

#proccesing and printout
if resto == 0:
    print 'el numero %4d es el MCD de ambos' %num2
elif resultado == 1 :
    print 'el numero %4d es el MCD de ambos' %resultado
elif resultado > 1:
    solucion = resto - resultado
    print 'el numero %4d es el MCD de ambos' %solucion
else:
    print 'el numero %4d es el MCD de ambos' %resto
    
        
        

    
