# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 07:58:04 2013

@author: daniel
"""
#programa: funciones_calificaciones_342.py
#programa con menu de opciones
#ejercicio 342

#definir funciones
def agrega(alumnos, notas):
    print
    nombre = raw_input('Nombre del Estudiante: ')
    alumnos.append(nombre)
    nota = float(raw_input('Nota del Estudiante: '))
    notas.append(nota)
    return alumnos, notas
def listados(alumnos, notas):
    nueva_lista = []
    for i in range(0, len(alumnos)):
        nueva_lista += (alumnos[i], notas[i])
    return nueva_lista
def media(notas):
    elemento1 = 0
    for elemento in notas:
        elemento1 = elemento1 + elemento
        promedio = elemento1 / len(notas)
    return promedio
def aprobados(notas, minima):
    num = 0
    for i in range(0, len(notas)):
        if notas[i] > minima:
            num += 1
    return num
def mejor_notas(alumnos, notas):
    mayor = max(notas)
    estudiantes = []
    for i in range(0,len(notas)):
        if notas[i] == mayor:
            estudiantes.append(alumnos[i])
    return estudiantes        
def medio(alumnos, notas):
    estudiantes =[]
    promedio = media(notas)
    for i in range(0, len(notas)):
        if notas[i] >= promedio:
            estudiantes.append(alumnos[i])
    return estudiantes
def consulta(alumnos, notas):
    nombre = ""
    while nombre not in alumnos:
        print
        nombre = raw_input('Nombre del Estudiante: ')
        for i in range(0, len(alumnos)):
            if alumnos[i] == nombre:
                nota = notas[i]
    return nota

#cuerpo del programa
#menu de opciones 
while True:
    print """
   Alumnos - Calificaciones
   
1) Ingresa alumno y su calificacion
2) Lista de estudiantes con sus calificaciones
3) Calcula la media de las calificaciones
4) Calcula numero de aprobados
5) Estudiantes con mejor calificacion
6) Estudiantes con calificacion superior a la media
7) Nota de un estudiante determinado
8) Finalizar la ejecucion del programa
"""
#data input
    opcion = input("Elija una opcion: ")
    print
    nombres = ['Tigre', 'Oso', 'Mafalda', 'Auca', 'Leti', 'Daniel']
    calificaciones = [8.0, 9.0, 10.0, 8.0, 9.0, 8.0]
    minimo = 9.0

#activa funciones
    if opcion == 1:
        print agrega(nombres, calificaciones)
    elif opcion == 2:
        print 'Listado de Estudiantes y su nota:' 
        print listados(nombres, calificaciones) 
    elif opcion == 3:
        print 'La media de las calificaciones es %2.2f' % media(calificaciones)
    elif opcion == 4:
        print 'Cantidad de alumnos aprobados: ', aprobados(calificaciones, minimo)
    elif opcion == 5:
        print 'Alumnos con mejor calificacion: ', mejor_notas(nombres, calificaciones)
    elif opcion == 6:
        print 'Alumnos con calificacion superior a la media: ', medio(nombres, calificaciones)
    elif opcion == 7:
        print 'Listado: ', nombres, consulta(nombres, calificaciones)        
    elif opcion == 8:
        print 'Finaliza la aplicacion, gracias'
        break
    else:
        print "opcion incorrecta"