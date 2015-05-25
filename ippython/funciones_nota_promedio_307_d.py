# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:32:26 2013

@author: daniel
"""

#programa: funciones_nota_promedio_307_d.py
#hay una lista de alumnos y una lista con sus respectiva notas
#generar un listado de los que aprobaron igual o mayor al promedio
#ejercicio 307D

#procedimiento <aprobaron>
def aprobaron(alumnos, calificaciones):
    listado = []
    promedio = (max(calificaciones) + min(calificaciones)) / 2
    for i in range(len(calificaciones)):
        if calificaciones[i] >= promedio:
            listado.append(alumnos[i])
    print 'Listado de aprobados: ', listado

#cuerpo del programa

#data input
nombres = ['Tigre', 'Oso', 'Mafalda', 'Leti', 'Daniel']
calificaciones = [7.0, 9.0, 10.0, 9.0, 8.0]

#activa la funcion
aprobaron(nombres, calificaciones)