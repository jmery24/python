# -*- coding: utf-8 -*-
"""
Created on Thu May 23 06:11:49 2013

@author: daniel
"""

#programa: funeciones_raizenesima_295.py
#la funcion calcula el valor: raiz enesima de un valor x, dados (n, x)
#ejercicio 295

#define funcion raiz_n_esima
def raiz_n_esima(x, n):
    calculo = x**(1.0/n)
    return calculo
    
#cuerpo del programa
#data input
numero = float(raw_input('El valor del numero: '))
enesima = int(raw_input('El valor de <n>: '))

#activa la funcion
print 'La raiz %i de %f es: %f' %(enesima, numero, raiz_n_esima(numero, enesima))