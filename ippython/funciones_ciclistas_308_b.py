# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:26:35 2013

@author: daniel
"""

#programa: funciones_ciclistas_308_b.py
#lista de ciclistas, lista con sus tiempos y numero de etapa
#nombre del ganador de la etapa ingresada
#ejercicio 308B

#define la funcion <etapas>
def etapas(lista, valores, num):
    tiempos = []
    for i in range(len(valores)):
        tiempos.append(valores[i][num-1])
        minimo = min(tiempos)
        for j in range(len(tiempos)):
            if tiempos[j] == minimo:
                nombre = lista[j]
    return nombre     
        
#cuerpo principal del programa
#data input
ciclistas = ['Tigre', 'Oso', 'Auca']
tiempo = [[10092.0, 12473.1, 13732.3, 10232.1, 10392.3],
          [11726.2,11161.2, 12272.1, 11292.0, 12534.0],
          [10193.4, 10292.1, 11712.9, 10133.4, 11632.0]]
etapa = int(raw_input('Numero de Etapa: '))
        
#activa funcion <etapas>
print 'El ganador de la vuelta es : ', etapas(ciclistas, tiempo, etapa)        