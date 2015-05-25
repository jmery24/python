# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:59:26 2013

@author: daniel
"""

#programa: funciones_exponencial.py
#definir una funcion para el calculo exponencial

#definir funciones
#definir funcion <elevado>
def elevado(a, k):
    productorio = 1.0
    for i in range(1, k+1):
        productorio *= a
    return productorio
#definir funcion factorial
def factorial(k):
    productorio = 1.0
    for i in range(1, k+1):
        productorio *= i
    return productorio
#definir funcion <exponencial>
def exponencial(a, n):
    sumatorio = 0.0
    for k in range(n):
        sumatorio += elevado(a, k) / factorial(k)
    return sumatorio
    
#cuerpo del programa

#input

#output & activa funcion
     