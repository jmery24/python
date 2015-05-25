# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:55:54 2013

@author: daniel
"""

#programa: funciones_ciclistas_308_a.py
#lista de ciclistas y una lista con sus tiempos
#nombre del ganador cuyos tiempos sumados en las 5 etapas es minimo
#ejercicio 308A

#define la funcion <etapas>
def etapas(lista, valores):
    tiempos = []
    for i in range(len(valores)):
        tiempos.append(sum(valores[i]))
        print tiempos
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
        
#activa funcion <etapas>
print 'El ganador de la vuelta es : ', etapas(ciclistas, tiempo)        