# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 07:30:41 2013

@author: daniel
"""

#programa: funciones_duplica_numero_348.py
#definir una funcion que duplique los valores de la lista original
#modificando la lista original
#ejercicio 348

#definir funcion <duplica>
def duplica(lista):
    for i in range(len(lista)):        
        lista[i] = lista[i]*2                
    return lista
    
#cuerpo del programa
#input
numeros = [1, 6, 15, 25, 30, 40]

#activa procedimiento
print 'Numeros originales: ', numeros
print
print 'Numeros duplicados: ', duplica(numeros)
print
print 'lista original modificada: ', numeros