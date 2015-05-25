# -*- coding: utf-8 -*-
"""
Created on Mon May 27 06:05:29 2013

@author: daniel
"""

#programa: funciones_muestra_nota.py
#hay una lista de alumnos y una lista con sus respectiva notas
#se introduce un nombre y muestra el nombre y la nota si pertenece a la clase

#definimos funcion <muestra_nota>
def muestra_nota(alumnos, notas, alumno_buscado):
    encontrado = False
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            print alumno_buscado, notas[i]
            encontrado = True
            break #una vez encontrado el nombre no sigue iterando
    if not encontrado:
        print 'El alumno %s no pertenece a la clase' %alumno_buscado
        
#variante mas reducida que la version <muestra_nota>
def nota_alumno(alumnos, notas, alumno):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno:
            print alumno, notas[i]
            return
    print 'El alumno %s no pertenece a la clase' %alumno
    
            
    

#cuerpo del programa

#data input
nombres = ['Tigre', 'Oso', 'Mafalda', 'Leti', 'Daniel']
calificaciones = [8.0, 9.0, 10.0, 9.0, 8.0]
nombre = raw_input('Nombre del Alumno: ')
print

#activa la funcion
muestra_nota(nombres, calificaciones, nombre)
print
nota_alumno(nombres, calificaciones, nombre)