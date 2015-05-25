# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 07:24:53 2013

@author: daniel
"""
# programa: registros_evolucion.py
# muestra la evolucion para trabajar con registros

#-----------------------------METODO SIMPLE----------------------------------
# forma clasica: ingresa 6 datos para 6 variables
# definir funcion <muestra_mascota>
def muestra_mascota(nombre, clase, edad):
    print 'Nombre: ', nombre
    print 'Clase: ', clase
    print 'Edad: ', edad
# Programa
# input
nombre_1 = 'Tigre'
clase_1 = 'Gato'
edad_1 = 1

nombre_2 = 'Oso'
clase_2 = 'Perro'
edad_2 = 17
# activa funcion
print '-------------'
print 'METODO SIMPLE'
muestra_mascota(nombre_1, clase_1, edad_1)
print
muestra_mascota(nombre_2, clase_2, edad_2)

#------------------------------METODO DOS LISTAS-----------------------------
# Utiliza 2 listas y tres elementos por cada lista
# definir funcion <mostrar_mascota>
def mostrar_mascota(mascotas):
    print 'Nombre: ', mascotas[0]
    print 'Clase: ', mascotas[1]
    print 'Edad: ', mascotas[2]    
# Programa
# input
tigre = ['Tigre', 'Gato', 1]
oso = ['Oso', 'Perro', 17]
# activa funcion
print '-----------------'
print 'METODO DOS LISTAS'
mostrar_mascota(tigre)
print
mostrar_mascota(oso)
 
#-----------------------------METODO TRES LISTAS-----------------------------
# Utiliza 3 listas, dos de ellas con tres elementos y una con 2 elementos
def mostrando_mascota(mascotas):
    print 'Mascotas: ', mascotas
    print mascotas[0][0], '=', mascotas[0]
    print mascotas[1][0], '=', mascotas[1]
# Programa
# input
tigre = ['Tigre', 'Gato', 1]
oso = ['Oso', 'Perro', 17]
mascotas = [tigre, oso]
# activa funcion
print '------------------'
print 'METODO TRES LISTAS'
mostrando_mascota(mascotas)

#------------------------------METODO UNA MATRIZ-----------------------------
# utiliza matrices
# definir funcion <muestra_mascotita>
def muestra_mascotita(mascotas):
    for i in mascotas:
        print i
# Programa
# input
animales = [['Tigre', 'Gato', 1], ['Oso', 'Perro', 17]]
# activa funcion
print '-----------------'
print 'METODO UNA MATRIZ'
muestra_mascotita(animales)

#-----------------------------METODO DOS REGISTROS---------------------------
# utiliza registros
# llama modulo record
from record import record
# definir funcion <muestra_animales>
def muestra_animales(mascotas):
    print 'Nombre: ', mascotas.nombre
    print 'Clase: ', mascotas.clase
    print 'Edad: ', mascotas.edad
# definir clase <Mascota>
class Mascota(record):
    nombre = ''
    clase = ''
    edad = 0
# input
tigre =  Mascota(nombre = 'Tigre', clase = 'Gato', edad = 1)
oso = Mascota(nombre = 'Oso', clase = 'Perro', edad = 17)
# activa funcion
print '--------------------'
print 'METODO DOS REGISTROS'
muestra_animales(tigre)
muestra_animales(oso)
  
#------------------------------METODO UN REGISTRO----------------------------
# utiliza variante de regisros
# definir funcion <muestra_animalitos>
def muestra_animalitos(mascotas):
    for i in range(len(mascotas)):
        print 'Nombre: ', mascotas[i].nombre
        print 'Clase: ', mascotas[i].clase
        print 'Edad: ', mascotas[i].edad
# definir clase <Animal>
class Animal(record):
    nombre = ''
    clase = ''
    edad = 0
# input
listado_mascotas = [Animal(nombre = 'Tigre', clase = 'Gato', edad = 1),\
                    Animal(nombre = 'Oso', clase = 'Perro', edad = 17)]  
# activa funcion
print '------------------'
print 'METODO UN REGISTRO'
muestra_animalitos(listado_mascotas)
#----------------------------------------------------------------------------                  