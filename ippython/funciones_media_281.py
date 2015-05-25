# -*- coding: utf-8 -*-
"""
Created on Thu May 16 07:47:51 2013

@author: daniel
"""

#programa: funciones_media_281.py
#la funcion calcula la media aritmetica de una lista
#ejercicio 281

#funcion <sumatorio>
def sumatorio(lista):
    suma = 0
    for i in lista:
        suma += i/2
    return suma
    
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
print 'la media aritmetica de la lista', listado,  'es: ', sumatorio(listado)