# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 06:17:18 2013

@author: daniel
"""

#programa: funciones_NumerosPrimos_335.py
#la funcion devuelve una lista con los numeros impares  
#ejercicio 335

#definir la funcion <no_repetidos>
def primos(lista):
    resultado = []
    primos = []
    for elementos in lista:
        for i in range(2, elementos):
            if elementos % i == 0 and elementos not in resultado:
                resultado.append(elementos)
    for elemento_1 in lista:
        for elemento in resultado:
            if elemento_1 not in resultado and elemento_1 not in primos:
                primos.append(elemento_1)
    return primos
       
#cuerpo del programa
#data input
cantidad = int(raw_input('Cantidad de elementos de la lista: '))
listado = []

for i in range (0, cantidad):
    elemento = int(raw_input('Escribe un elemento: '))
    listado.append(elemento)
    
#activa la funcion
print
print 'listado original de numeros'
print listado
print
print 'lista de numeros primos'
print primos(listado)
