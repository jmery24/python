# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:50:39 2013

@author: daniel
"""

#programa: funciones_ciclistas_308_c.py
#lista de ciclistas y lista con sus tiempos
#nombre del ganador de cada etapa
#ejercicio 308C
#NO FUNCIONA

#define la procedimiento <etapas>
def etapas(lista, valores):
    nula = []
    for i in range(5):
        nula.append([0]*3)
    for j in range(5):
        for k in range(3):
            nula[j][k] = valores[k][j]
    nombre = ''
    tiempos = 0
    for l in range(len(nula)):
        tiempos = min(nula[l])
        for m in range(len(valores)):
            if tiempos == nula[l][m]:
                nombre = valores[m]
    print nula[0][0]    
    print tiempos
    print lista[m]      
        
#cuerpo principal del programa
#data input
ciclistas = ['Tigre', 'Oso', 'Auca']
tiempo = [[10092.0, 12473.1, 13732.3, 10232.1, 10392.3],
          [11726.2,11161.2, 12272.1, 11292.0, 12534.0],
          [10193.4, 10292.1, 11712.9, 10133.4, 11632.0]]
        
#activa funcion <etapas>
etapas(ciclistas, tiempo)        