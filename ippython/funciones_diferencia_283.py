# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:40:33 2013

@author: daniel
"""
#programa: funciones_diferencia_283.py
#la funcion calcula la diferencia del maximo numero y su contiguo anterior
#el numero maximo al comienzo de la lista calcula la resta 
#del primero y el ultimo de la lista
#ejercicio 283

#funcion: num_maximo
def num_maximo(lista):
    candidato = lista[0]
    flag = 0
    for i in range(0, len(lista)):
        if lista[i] > candidato:
            candidato = lista[i]
            flag = i            
        else:
            candidato
    return candidato - lista[flag-1]
    
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
print 'la diferencia entre el maximo y anterior es: ', num_maximo(listado)    