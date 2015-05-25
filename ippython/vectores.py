# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 08:18:45 2013

@author: daniel
"""

# vectores.py
#—————————————————-
# Modulo vectores
#—————————————————-
# Proporciona constantes y funciones para el calculo vectorial en 3 dimensiones.
#—————————————————-
# Constantes que exporta:
# v_i, v_j, v_k: vectores unidad
#
# Funciones que exporta:
# v_lee_vector:
# sin parametros
# devuelve un vector leido de teclado que se pide al usuario
#
# v_muestra_vector(v):
# muestra por pantalla el vector v con la notacion (x, y, z)
# no devuelve nada
#
# v_longitud(v):
# devuelve la longitud del vector v
#
# v_suma(u, v):
# devuelve el vector resultante de sumar u y v
#
# v_producto ̇escalar(u, v):
# devuelve el escalar resultante del producto escalar de u por v
#
# v_producto ̇vectorial(u, v):
# devuelve el vector resultante del producto vectorial de u por v
#
# v_son ̇perpendiculares(u, v):
# devuelve cierto si u y v son perpendiculares, y falso en caso contrario
#—————————————————
# importa del modulos <math> la funcion <sqrt>
from math import sqrt

# Constantes
v_i =[1, 0, 0]
v_j =[0, 1, 0]
v_k =[0, 0, 1]

# Funciones de entrada/salida
def v_lee_vector():
    x = float(raw_input('Componente x: '))
    y = float(raw_input('Componente y: '))
    z = float(raw_input('Componente z: '))
    return [x, y, z]

def v_muestra_vector(v):
    print '(%2.2f, %2.2f, %2.2f)' % (v[0], v[1], v[2])

# Funciones de calculo
def v_longitud(v):
    return sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def v_suma(u, v):
    return [ u[0] + v[0], u[1] + v[1], u[2] + v[2] ]

def v_producto_escalar(u, v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def v_producto_vectorial(u, v):
    resultado_x = u[1]*v[2] - u[2]*v[1]
    resultado_y = u[2]*v[0] - u[0]*v[2]
    resultado_z = u[0]*v[1] - u[1]*v[0]
    return [resultado_x, resultado_y, resultado_z]

# Predicados
def v_son_perpendiculares(u, v):
    return v_producto_escalar(u, v) == 0
    
#prueba de las funciones del modulo, no funciona cuando se lo invoca
if __name__ == '__main__':
    vector_1 = (0.0, 4.0, 0.0)
    vector_2 = (3.0, 0.0, 0.0)
    print 'Muestra vector_1: ', v_muestra_vector(vector_1)
    print 'Muestra vector_2: ', v_muestra_vector(vector_2)
    print 'Longitud del vector_1: ', v_longitud(vector_1)
    print 'Longitud del vector_2: ', v_longitud(vector_2)
    print 'Suma de vectores: ', v_suma(vector_1, vector_2)
    print 'Producto escalar: ', v_producto_escalar(vector_1, vector_2)
    print 'Producto vectorial: ', v_producto_vectorial(vector_1, vector_2)
    print 'Son perpendiculares ?', v_son_perpendiculares(vector_1, vector_2)