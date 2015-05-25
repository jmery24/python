# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:14:35 2013

@author: daniel
"""

#programa: funciones_producto_282.py
#la funcion calcula el producto de los elementos de una lista
#ejercicio 282

#funcion <producto>
def producto(lista):
    producto = 1
    for i in lista:
        producto *= i
    return producto
    
#cuerpo del programa
#data iinput
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#construye el listado desde el teclado
listado = []
for i in range(num):
    elemento = float(raw_input('Elemento: '))
    listado.append(elemento)


#activa la funcion
print
print 'el producto de la lista', listado,  'es: ', producto(listado)