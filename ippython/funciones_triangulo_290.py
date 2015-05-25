# -*- coding: utf-8 -*-
"""
Created on Wed May 22 05:34:48 2013

@author: daniel
"""

#programa: funciones_triangulo_290.py
#define una funcion que calcule el perimetro de un triangulo
#ejercicio 290

#funcion <perimetro>
def perimetro(listado):
    perimetro = listado[0] + listado[1] + listado[2]
    return perimetro
    
#cuerpo del programa
#data input
lista = []
for i in range(3):
    lado = int(raw_input('Valor del lado: '))
    lista.append(lado)
    
#activa la funcion
print
print 'El perimetro del triangulo es: ', perimetro(lista)