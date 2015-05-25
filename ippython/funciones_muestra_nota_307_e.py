# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:40:31 2013

@author: daniel
"""

#programa: funciones_muestra_nota_307_e.py
#hay una lista de alumnos y una lista con sus notas
#introduce un nombre y muestra el nombre y la nota si pertenece a la lista
#ejercicio 307E

#definimos funcion <muestra_nota>
def nota_alumno(alumnos, notas, alumno):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno:
            return notas[i]
            
#cuerpo del programa

#data input
nombres = ['Tigre', 'Oso', 'Mafalda', 'Leti', 'Daniel']
calificaciones = [8.0, 9.0, 10.0, 9.0, 8.0]
nombre = raw_input('Nombre del Alumno: ')
print

#activa la funcion
print 'la nota es: ', nota_alumno(nombres, calificaciones, nombre)