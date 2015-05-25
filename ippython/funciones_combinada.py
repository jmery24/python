# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:16:44 2013

@author: daniel
"""

#programa: funciones_combinada.py
#funcion lee un numero entero del teclado
#funcion que evalua si el numero ingresado es par


#define funcion <lee_entero>
def lee_entero():
    return int(raw_input('Ingresa un numero entero: '))
    
#define funcion <es_par>
def es_par(num):
    return num % 2 == 0
    
#ambas funciones en una
def ambas():
    numero = int(raw_input('Ingresa un numero: '))
    print
    return numero % 2 == 0
    
#cuerpo del programa
#activa la funciones
a = lee_entero()
print
print 'El numero entero ingresado es: ', a
print
print 'El numero ingresado es par? ', es_par(a)
print
print ambas()
print
 