# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:03:27 2013

@author: daniel
"""

#programa: funciones_maxima_nota_307_c.py
#hay una lista de alumnos y una lista con sus respectiva notas
#generar un listado de los que aprobaron con maxima nota
#ejercicio 307C

#procedimiento <maxima>
def maxima(alumnos, calificaciones):
    listado = []
    nota_maxima = max(calificaciones)
    for i in range(len(calificaciones)):
        if calificaciones[i] == nota_maxima:
            listado.append(alumnos[i])
    print 'Listado de aprobados: ', listado

#cuerpo del programa

#data input
nombres = ['Tigre', 'Oso', 'Mafalda', 'Leti', 'Daniel']
calificaciones = [8.0, 9.0, 10.0, 9.0, 8.0]

#activa la funcion
maxima(nombres, calificaciones)