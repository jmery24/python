# -*- coding: utf-8 -*-
"""
Created on Mon May 27 07:11:55 2013

@author: daniel
"""

#programa: funciones_aprobaron_307.py
#hay una lista de alumnos y una lista con sus respectiva notas
#introducir la nota de aprobacion y exhibir la lista de los que aprobaron
#ejercicio 307

#procedimiento <aprobaron>
def aprobaron(alumnos, calificaciones, nota):
    aprueban = []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= nota:
            aprueban.append(alumnos[i])
    print 'Listado de aprobados: ', aprueban

#cuerpo del programa

#data input
nombres = ['Tigre', 'Oso', 'Mafalda', 'Leti', 'Daniel']
calificaciones = [8.0, 9.0, 10.0, 9.0, 8.0]
minimo = float(raw_input('Nota minima de aprobacion: '))
print

#activa la funcion
aprobaron(nombres, calificaciones, minimo)
print