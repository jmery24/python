# -*- coding: utf-8 -*-
"""
Created on Mon May 13 06:35:03 2013

@author: daniel
"""

#programa: funciones_maximo.py
#dada una lista numerica definir una funcion que seleccione el numero mayor


#definir funcion <maximo>, no contempla valor nulo (0)
def maximo(lista):
    candidato = lista[0]
    for elemento in lista:
        if elemento > candidato:
            candidato = elemento
    return candidato
    
#funcion alternativa para valor nulo (0): num_maximo
#esta funcion solo funciona si hay entrada de listado por programa no por
#teclado
def num_maximo(lista):
    if len(lista) > 0:
        candidato = lista[0]
        for elemento in lista:
            if elemento > candidato:
                candidato = elemento
    else:
        candidato = None
    return candidato


#cuerpo del programa
#data input
num = int(raw_input('Cantidad de elementos en la lista: '))
print

#construye la lista desde el teclado
listado = []
for i in range(num):
    elemento = int(raw_input('Elemento: '))
    listado.append(elemento)

#activa funcion <num_maximo>
print
print 'Numero mayor de la lista es: ', num_maximo(listado)        

#activa la funcion <maximo>
print
print 'El numero maximo de la lista es: ', maximo(listado)
      