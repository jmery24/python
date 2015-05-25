# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 07:16:02 2013

@author: daniel
"""

#programa: funciones_duplica_numero_349.py
#definir una funcion que duplique los valores de la lista original
#sin modificar la lista original
#ejercicio 349

#definir funcion <duplica>
def duplica(lista):
    nueva = []
    for i in range(len(lista)):
        nueva.append(lista[i]*2)        
    return nueva
    
#cuerpo del programa
#input
numeros = [1, 6, 15, 25, 30, 40]

#activa procedimiento
print 'Numeros originales: ', numeros
print
print 'Numeros duplicados: ', duplica(numeros)
print
print 'lista original sin modificar: ', numeros