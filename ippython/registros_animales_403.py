# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:37:49 2013

@author: daniel
"""

#programa: registros_animales_403.py
#print el registro de animales mayores de 10 anios
#ejercicio 403
#llama modulo record
from record import record
#definir funcion <muestra_animales>
def muestra_animales(mascotas):
    if mascotas.edad > 10:
        print 'Nombre: ', mascotas.nombre
        print 'Clase: ', mascotas.clase
        print 'Sexo: ', mascotas.sexo
        print 'Edad: ', mascotas.edad
class Mascota(record):
    nombre = ''
    clase = ''
    sexo = ''
    edad = 0
#input
tigre =  Mascota(nombre = 'Tigre Mery', clase = 'Gato', sexo = 'Macho', edad = 1)
oso = Mascota(nombre = 'Oso Mery', clase = 'Perro', sexo = 'Macho', edad = 17)
#activa funcion
print '-------'
print 'LISTADO'
print
muestra_animales(tigre)
print
muestra_animales(oso)
#--------------------------------------------------------