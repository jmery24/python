# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 07:15:33 2013

@author: daniel
"""

#programa: funciones_Nombres_334.py
#lista con nombres
#seleccionar una <letra>
#la funcion devuelve una lista con los nombres que comiencen con la <letra>  
#ejercicio 334

#definir la funcion <no_repetidos>
def nombres(lista, letra):
    resultado = []
    for i in range(0, len(lista)):
        if lista[i][0] == letra:
            resultado.append(lista[i])           
    return resultado
    
#cuerpo del programa
#data input
cantidad = int(raw_input('Cantidad de elementos de la lista A: '))
listado = []
for i in range (0, cantidad):
    elemento = raw_input('Escribe un nombre: ')
    listado.append(elemento)
letra = raw_input('Escribe una letra: ')
        
#activa la funcion
print
print 'listado original de nombres'
print listado
print
print 'lista con nombres que empiecen con la letra: ', letra
print nombres(listado, letra)