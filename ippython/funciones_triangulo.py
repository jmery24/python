# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:18:48 2013

@author: daniel
"""

#programa: funciones_triangulo.py
#define tres funciones para calcular el area del triangulo < a, b, c >
#calcular el angulo opuesdto al lado <a>
#definir en un menu que calculo queremos realizar

#importamos del modulo <math> las funciones: sqrt, asin, pi
from math import sqrt, asin, pi

#definimos funciones

#funcion <area_triangulo>
def area_triangulo(a, b, c):
    s = (a + b + c) / 2.0
    if s > a and s > b and s > c:
        return sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return 0
#funcion <angulo_alfa>
def angulo_alfa(a, b, c):
    s = area_triangulo(a ,b, c)
    return 180 / pi * asin (2.0 * s / (b * c))
    
# funcion <menu>, es una funcion sin argumentos
def menu():
    opcion = 0
    while opcion != 1 and opcion != 2:
        print '1) Calcular el area del triangulo'
        print '2) Calcular el angulo opuesto al primer lado'
        print
        opcion = int(raw_input('Escoge opcion: '))
    return opcion

#cuerpo del programa
#data input
lado1 = 0
lado2 = 0
lado3 = 0
while lado1 <= 0 or lado2 <= 0 or lado3 <= 0: #cualquier lado debe ser > 0 
    lado1 = float(raw_input('Valor lado <a>: '))
    lado2 = float(raw_input('Valor lado <b>: '))
    lado3 = float(raw_input('Valor lado <c>: '))
    print 'el valor de cualquier lado no puede ser cero o negativo'
print

#activa funcion sin argumentos <menu>
s = menu()

if s == 1:
    resultado = area_triangulo(lado1, lado2, lado3) #activa funcion 
else:
    resultado = angulo_alfa(lado1, lado2, lado3) #activa funcion

#output data
print
print 'Escogiste opcion: ', s
print 'El resultado es: ', resultado
    
    
    