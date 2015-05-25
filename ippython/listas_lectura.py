# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:27:20 2013

@author: daniel
"""

#programa:listas_lectura.py
#para crear una lista desde el teclado

#utilizando concatenacion
lista = []
for i in range(5):
    elemento = int(raw_input('dame un elemento: '))
    lista = lista + [elemento]
print lista    

#utilizando append()
lista = []
for j in range(6):
    elemento = int(raw_input('dame un elemento: '))
    lista.append(elemento)
print lista

#variante donde la cantidad de elementos de la lista es una variable
lista = []
numero = int(raw_input('cantidad de elementos de la lista: '))
for k in range(numero):
    elemento = int(raw_input('dame un elemento: '))
    lista.append(elemento)
print lista

#variante <while>, se introducen elementos hasta que el valor sea < 0
lista = []
numero = int(raw_input('dame un elemento: '))
while numero >= 0:
    lista.append(numero)
    numero = int(raw_input('dame un elemento: '))
print lista