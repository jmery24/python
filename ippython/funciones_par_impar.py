# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:32:56 2013

@author: daniel
"""

#programa: funciones_par_impar.py
#definir dos funcionescon recursividad indirecta
#verifica si un numero es par o impar

#definir las funciones
#definir funcion <par>
def par(n):
    if n == 0:
        return True
    else:
        return impar(n-1)
#definir funcion <impar>
def impar(n):
    if n == 0:
        return False
    else:
        return par(n-1)
        
#cuerpo del programa
#input
numero = int(raw_input('Escriba un numero: '))

#activa funcion y output
print 'el numero', numero, 'es par?', par(numero)           