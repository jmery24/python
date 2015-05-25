# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:34:39 2013

@author: daniel
"""
#programa: funciones_sumatorio_277.py
#la funcion realiza un sumatorio de las diferencias 
#entre dos numeros contiguos
#ejercicio 277

def sumatorio(num):
    suma =0
    for i in range(0, len(num)):
        suma += num[i-1] - num[i]
        return suma
    
#cuerpo del programa
#data input
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#construye la lista desde el teclado
lista = []
for i in range(num):
    elemento = int(raw_input('Elemento: '))
    lista.append(elemento)

#activa la funcion
print 'la suma de las diferencias contiguas es: ', sumatorio(lista)