# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:48:00 2013

@author: daniel
"""
#programa: registros_test_402.py
#ejercicio 402
from record import record
#definir funcion <muestra_animales>
def muestra_animales(mascotas):
    print mascotas.nombre
    print 'Tipo: ', mascotas.tipo
    print 'Sexo: ', mascotas.sexo
    print 'Edad: ', mascotas.edad
class Mascota(record):
    nombre = ''
    tipo = ''
    sexo = ''
    edad = 0
#input
listado = [[Mascota(nombre = 'Tigre', tipo = 'gato', sexo = 'M', edad = 1)],\
          [Mascota(nombre = 'Oso', tipo = 'perro', sexo = 'M', edad = 17)],\
          [Mascota(nombre = 'Auca', tipo = 'perro', sexo = 'H', edad = 28)]]
#output
print '-------'
print 'LISTADO'
print
for i in range(len(listado)):
    muestra_animales(listado[i][0]) #funciona si solo si: listado[i][0] 