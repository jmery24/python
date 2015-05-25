# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:04:41 2013

@author: daniel
"""

#programa: funciones_mcd.py
#definir funcion que calcula el MCD de dos numeros <m> y <n>

#definir funciones
#definir funcion <minimo>
def minimo(a, b):
    if a < b:
        return a
    else:
        return b
        
#definir funcion <maximo>
def maximo(a, b):
    if a > b:
        return a
    else:
        return b
            
#definir funcion <mcd>
def mcd(m, n):
    menor = minimo(m, n)
    mayor = maximo(m, n)
    resto = mayor % menor
    if resto == 0:
        return menor
    else:
        return mcd(menor, resto)
        
#cuerpo principal del programa

#input
numero_a = int(raw_input('Valor de A: '))
numero_b = int(raw_input('Valor de B: '))
print

#activa funcion y output
print 'El MCD de %i y %i es: %i' %(numero_a, numero_b, mcd(numero_a, numero_b))                