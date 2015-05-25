# -*- coding: utf-8 -*-
"""
Created on Mon May 27 07:24:28 2013

@author: daniel
"""

#programa: funciones_aprobaron_307_a.py
#listado de notas
#introducir la nota minima y calcular cuantos aprobaron
#ejercicio 307_a

#procedimiento <cantidad>
def cantidad(calificaciones, nota):
    aprobados = 0
    for i in range(len(calificaciones)):
        if calificaciones[i] > nota:
            aprobados += 1
    print 'Cantidad de aprobados: ', aprobados

#cuerpo del programa

#data input
calificaciones = [7.0, 9.0, 10.0, 8.0, 6.0]
minimo = float(raw_input('Nota minima de aprobacion: '))
print

#activa la funcion
cantidad(calificaciones, minimo)
print