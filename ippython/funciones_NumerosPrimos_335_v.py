# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 07:35:14 2013

@author: daniel
"""

#programa: funciones_NumerosPrimos_335.py
#la funcion devuelve una lista con los numeros impares  
#ejercicio 335

#definir la funcion <no_repetidos>
def primos(lista):
    resultado = []
    for elemento in lista:
        for i in range(2, elemento):
            if elemento % i == 0 and elemento not in resultado:
                resultado.append(elemento)
    return resultado
    
#definir funcion de resta de listas
def resta(listado, lista):
    primos = []
    for elemento_1 in listado:
        for elemento in lista:
            if elemento_1 not in lista and elemento_1 not in primos:
                primos.append(elemento_1)
    return primos
   
#cuerpo del programa
#data input
cantidad = int(raw_input('Cantidad de elementos de la lista: '))
listado = []

for i in range (0, cantidad):
    elemento = int(raw_input('Escribe un elemento: '))
    listado.append(elemento)
    
no_primos = primos(listado)
        
#activa la funcion
print
print 'listado original de numeros'
print listado
print
print 'lista de numeros primos'
print resta(listado, no_primos)
