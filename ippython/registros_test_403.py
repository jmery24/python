# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:15:01 2013

@author: daniel
"""

#programa: registros_test_403.py
#ejercicio 403
from record import record
#definir funcion <muestra_animales>
def menor_edad(mascotas):
    if mascotas.edad  < 6:
        print mascotas.nombre, ':',
        print True
    else:
        print mascotas.nombre, ':',        
        print False
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
print '--------------------'
print 'Es menor de 6 anios?'
print
for i in range(len(listado)):
    menor_edad(listado[i][0]) #funciona si solo si: listado[i][0] 