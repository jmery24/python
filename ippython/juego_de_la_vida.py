# -*- coding: utf-8 -*-
"""
Created on Mon May  6 07:22:57 2013

@author: daniel
"""

#programa:juego_de_la_vida.py

#datos para una matriz T de filas X columnas  M(fXc)
print 'La matriz debe ser igual o mayor T(7x7)'
filas = int(raw_input('Filas de la Matriz: '))
columnas = int(raw_input('Columnas de la Matriz: '))

#creamos una matriz nula T(f X c)
tablero = []
for i in range(filas):
    tablero.append([False] * columnas)
    
tablero[4][5] = True
tablero[5][5] = True
tablero[6][5] = True

#representar el tablero
for y in range(filas):
    for x in range(columnas):
        if tablero[y][x]:
            print '*',
        else:
            print '.',
    print
    
#reloj del juego
pulsos = 10
for t in range(pulsos):
    #preparar nuevo tablero
    nuevo = []
    for i in range(filas):
        nuevo.append([0] * columnas)

    #actualizar tablero
    for y in range(filas):
        for x in range(columnas):
            #calcular numero de vecinos que estamos visitando
            n = 0
            if y > 0 and x > 0 and tablero[y-1][x-1]:
                n += 1
            if x > 0 and tablero[y][x-1]:
                n += 1
            if y < filas-1 and tablero[y+1][x-1]:
                n += 1
            if y > 0 and tablero[y-1][x]:
                n += 1
            if y < filas-1 and x > 0 and tablero[y+1][x]:
                n += 1
            if y > 0 and x < columnas-1 and  tablero[y-1][x+1]:
                n += 1
            if x < columnas-1 and tablero[y][x+1]:
                n += 1
            if y < filas-1 and x < columnas-1 and tablero[y+1][x+1]:
                n += 1
                
                #aplicar reglas
                if tablero[y][x] and (n==2 or n==3): #supervivencia
                    nuevo[y][x] = True
                elif not tablero[y][x] and n==3: #nacimiento
                    nuevo[y][x] = True
                else:
                    nuevo[y][x] = False
    
    #actualizar tablero
    tablero = nuevo
    
    #representar tablero
    print 'Pulso', t+1
    for y in range(filas):
        for x in range(columnas):
            if tablero[y][x]:
                print '*',
            else:
                print '.',
        print
        
    
                    
                    
                
                
                
                
    