# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 07:06:18 2013

@author: daniel
"""

#programa: funciones_NumerosImpares_333.py
#la funcion devuelve una lista con los numeros impares  
#ejercicio 333

#definir la funcion <no_repetidos>
def impares(lista):
    resultado = []
    for elemento in lista:
        if elemento % 2 != 0:
            resultado.append(elemento)           
    return resultado
    
#cuerpo del programa
#data input
cantidad = int(raw_input('Cantidad de elementos de la lista: '))
listado = []
for i in range (0, cantidad):
    elemento = int(raw_input('Escribe un elemento: '))
    listado.append(elemento)
        
#activa la funcion
print
print 'listado original'
print listado
print
print 'lista con numeros impares'
print impares(listado)