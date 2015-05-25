# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:22:33 2013

@author: daniel
"""

#programa: funciones_diferencia_284.py
#la funcion calcula la diferencia del maximo el minimo numero 
#ejercicio 284

#funcion alternativa para valor nulo (0): maximo_minimo
def maximo_minimo(lista):
    mayor = lista[0]
    for maximo in lista:
        if maximo > mayor:
            mayor = maximo
        else:
            mayor
    menor = lista[0]
    for minimo in lista:
        if minimo < menor:
            menor = minimo
        else:
            menor
    return mayor - menor

#cuerpo del programa
#data input
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#construye la lista desde el teclado
listado = []
for i in range(num):
    elemento = int(raw_input('Elemento: '))
    listado.append(elemento)

#activa la funcion
print
print 'la diferencia maximo-minimo es: ', maximo_minimo(listado)    