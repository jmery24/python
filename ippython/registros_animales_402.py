# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 08:30:45 2013
@author: daniel
"""

#programa: registros_animales_402.py
#print el registro de animales, <agrega genero>
#ejercicio 402
#llama modulo record
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
tigre =  Mascota(nombre = 'Tigre', tipo = 'gato', sexo = 'M', edad = 1)
oso = Mascota(nombre = 'Oso', tipo = 'perro', sexo = 'M', edad = 17)
auca = Mascota(nombre = 'Auca', tipo = 'perro', sexo = 'H', edad = 28)
listado = [tigre, oso, auca]
#output
print '-------'
print 'LISTADO'
print
muestra_animales(tigre)
print
muestra_animales(oso)
print
for i in range(len(listado)):
    muestra_animales(listado[i])
#-------------------------------------------------------------    