# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 06:57:01 2013

@author: daniel
"""

#programa: funciones_calificaciones_357.py
#input: matriz mXn, datos por cada fila: numero alumno, calificaciones 
#examenes presentados, sino presento el examen la calificacion es -1
#definir 9 funciones para diferentes calculos
#ejercicio 357

#definir funciones
        #ejercicios_entregados
        #numero de alumno, cantidad ejercicios entregados
def ejercicios_entregados(matriz, columna, num):
    sum = 0
    for i in range(columna):
        if matriz[i][0] == num:
            for j in range(1, columna):
                if matriz[i][j] != num and matriz[i][j] != -1:
                    sum +=1
    return sum                
            
        #calificacion_media
        #numero alumno, calificacion media sobre los ejercicios entregados 
def calificacion_media(matriz, fila, columna, num):
    media = 0
    suma = 0
    for i in range(fila):
        if matriz[i][0] == num:
            for j in range(1, columna):
                if matriz[i][j] != num and matriz[i][j] != -1:
                    suma += matriz[i][j]
                    media = suma / (columna - 1)
    return media
        
        #calificacion_media_cero
#numero de alumno, media sobre los ejercicios entregados, <0> si falta uno
def calificacion_media_cero(matriz, fila, columna, num):
    media = 0
    suma = 0
    for i in range(fila):
        if matriz[i][0] == num:
            for j in range(1, columna):
                if matriz[i][j] != num and matriz[i][j] != -1:
                    suma += matriz[i][j]
                elif matriz[i][j] == -1:
                    return 0
                media = suma / (columna - 1)
    return media
    
        #media_tres_cinco
#todos los ejercicios y > 3.5 de promedio, cantidad de estudiantes
def media_tres_cinco(matriz, fila, columna):
    suma = 0
    resta = 0
    for i in range(fila):
        for j in range(1, columna):
            if matriz[i][j] >= 3.5:
                suma += 1
            else:
                resta += 1
                cantidad = (suma - resta) / (columna - 1)        
    return cantidad
    
    print 'opcion 4'
        #nota_media
#numero de ejercicio, calificacion media para los alumnos que lo presentaron
def nota_media(matriz, columna, fila, numero):
    T = []
    for i in range(m):
        T.append([0]*n)
    for i in range(m):
        for j in range(n):
            T[i][j] = M[j][i]
    num = numero -1
    nueva = []
    for i in range (1, fila):
        if i == num:
            for j in range (0, columna):
                nueva.append(T[i][j])
                promedio = sum(nueva) / len(nueva)
    return promedio
        #nota_alta
#numero de ejercicio, la nota mas alta
def nota_alta(matriz, fila, columna, numero):
    T = []
    for i in range(m):
        T.append([0]*n)
    for i in range(m):
        for j in range(n):
            T[i][j] = M[j][i]
    num = numero -1
    nueva = []
    for i in range (1, fila):
        if i == num:
            for j in range (0, columna):
                nueva.append(T[i][j])
                promedio = max(nueva)
    return promedio
        #nota_baja
#numero de ejercicio, la nota mas baja
def nota_baja(matriz, fila, columna, numero):
    T = []
    for i in range(m):
        T.append([0]*n)
    for i in range(m):
        for j in range(n):
            T[i][j] = M[j][i]
    num = numero -1
    nueva = []
    for i in range (1, fila):
        if i == num:
            for j in range (0, columna):
                nueva.append(T[i][j])
                promedio = min(nueva)
    return promedio    
            #presentaron
#numero de ejercicio, cantidad de estudiantes que lo presentaron
def presentaron(matriz, fila, columna, numero):
    T = []
    for i in range(m):
        T.append([0]*n)
    for i in range(m):
        for j in range(n):
            T[i][j] = M[j][i]
    num = numero -1
    nueva = []
    for i in range (1, fila):
        if i == num:
            for j in range (0, columna):
                if matriz[i][j] >= 0:
                    nueva.append(matriz[i][j])
                    cantidad = j + 1
    return cantidad                
#cuerpo del programa
#input: crea matriz
        #definimos tamanio de la matriz
print '   Matriz de (filas X columnas)'
n = int(raw_input('numero de filas: '))
m = int(raw_input('numero de columnas: '))
print
        #creamos una matriz nula
M = [[1.0, 4.0, 9.0], [2.0, 5.0, 7.0], [3.0, 8.0, -1.0]]
#for i in range(n): #creamos una matriz nula
#    M.append([0]*m)
        #leemos su contenido desde el teclado
#print '   Componentes de la matriz'
#for j in range(n):
#    for k in range(m):
#        M[j][k] = float(raw_input('Dame el componente (%d,%d): ' %(j,k)))
print
#print '   Matriz de',len(M), 'X', len(M[0])
print M

#crea menu
while True:
    print """
   Alumnos - Calificaciones
   
1) Numero de ejercicios entregados por alumno
2) Nota media de ejercicios entregados por alumno
3) Nota media si entrego todos los ejercicios, caso contrario <0>
4) Cantidad de alumnos que entregaron los ejercicios y >3.5 de promedio
5) Nota media de ejercicios entregados por numero de ejercicio
6) Nota mas alta para un ejercicio seleccionado
7) Nota mas baja para un ejercicio seleccionado
8) Cantidad de estudiantes que presentaron un ejercicio seleccionado
9) Salir del programa
 
"""
#input: selecciona opcion
    opcion = input("Elija una opcion: ")
    print
    
#activa funciones
    if opcion == 1:
        numero = int(raw_input('Numero del alumno: '))
        print 'Cantidad de Ejercicios entregados'
        print ejercicios_entregados(M, m, numero)
    elif opcion == 2:
        numero = int(raw_input('Numero del alumno: '))
        print 'Nota promedio del alumno' 
        print calificacion_media(M, n, m, numero) 
    elif opcion == 3:
        numero = int(raw_input('Numero del alumno: '))
        print 'Nota promedio por alumno, cero si falta un ejercicio' 
        print calificacion_media_cero(M, n, m, numero)
    elif opcion == 4:
        print 'Cantidad alumnos (todos los ejercicios y promedio >3.5'
        print media_tres_cinco(M, n, m)
    elif opcion == 5:
        num = int(raw_input('Numero de ejercicio: '))
        if num > 1:
            nota_promedio = nota_media(M, n, m, num)
        print 'Nota media ejercicio %d es %2.2f' %(num, nota_promedio)
    elif opcion == 6:
        num = int(raw_input('Numero de ejercicio: '))
        if num > 1:
            nota_promedio = nota_alta(M, n, m, num)
        print 'Nota alta ejercicio %d es %2.2f' %(num, nota_promedio)
    elif opcion == 7:
        num = int(raw_input('Numero de ejercicio: '))
        if num > 1:
            nota_promedio = nota_baja(M, n, m, num)
        print 'Nota baja ejercicio %d es %2.2f' %(num, nota_promedio)
    elif opcion == 8:
        num = int(raw_input('Numero de ejercicio: '))
        if num > 1:
            cantidad = presentaron(M, n, m, num)
        print 'Alumnos que presentaron ejercicio %d es %2.0f' %(num, cantidad)                
    elif opcion == 9:
        print 'Finaliza la aplicacion, gracias'
        break
    else:
        print "opcion incorrecta"    