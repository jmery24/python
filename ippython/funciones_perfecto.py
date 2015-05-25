# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:49:11 2013

@author: daniel
"""

#programa: funciones_perfecto.py
#calcula si un numero dado es perfecto
#o sea si sus divisores sumados son iguales al numero

#definir funcion <es_perfecto>
def es_perfecto(n):
    sumatorio = 0
    for i in range(1, n):
        if n % i == 0:
            sumatorio += i
    if sumatorio == n:
        return True
    else:
        return False
        
#funcion alternativa
def perfecto(num):
    sumatorio = 0
    for i in range(1, num):
        if num % i == 0:
            sumatorio += i
    return sumatorio == num
        
#cuerpo principal del programa        

#data input
numero = int(raw_input('Introduzca un numero: '))
print

#activa funcion
print 'Es el numero ', numero, 'perfecto? ', es_perfecto(numero)

#activa funcion alternativa
print 'Es el numero ', numero, 'perfecto? ', perfecto(numero)