# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:39:13 2013

@author: daniel
"""

#—————————————————
# Modulo: gravedad
# Proposito: proporciona algunas constantes y funciones sobre 
# fısica gravitatoria.
# Autor: Daniel Mery
#—————————————————
# Constantes exportadas:
# G: Constante de gravitacion universal.
# M_Tierra: Masa de la Tierra (en kilos).
# R_Tierra: Radio de la Tierra (en metros).
# M_Luna: Masa de la Luna (en kilos).
# R_Luna: Radio de la Luna (en metros).
#
# Funciones exportadas:
# fuerza_grav : calcula la fuerza gravitatoria existente entre dos cuerpos.
# entradas:
# M: masa de un cuerpo (en kg).
# m: masa del otro cuerpo (en kg).
# r: distancia entre ellos (en metros).
# salida:
# fuerza (en Newtons).
#
# distancia : calcula la distancia que separa dos cuerpos atraıdos 
# por una fuerza gravitatoria determinada
# entradas:
# M: masa de un cuerpo (en kg).
# m: masa del otro cuerpo (en kg).
# F : fuerza gravitatoria experimentada (en m).
# salida:
# distancia (en metros).
#
# velocidad_escape: calcula la velocidad necesaria para 
# escapar de la atraccion gravitatoria de un cuerpo esferico.
# entradas:
# M: masa del cuerpo (en kg).
# R: radio del cuerpo (en metros).
# salida:
# velocidad (en metros por segundo).
#————————————————–
# Historia:
# Creado el 13/11/2001 por Isaac
# Modificado el 16/06/2013 por Daniel Mery
# se incluyen las constantes M_Luna y R_Luna

#importa modulo math
from math import sqrt

#definir valor de constantes
G = 6.67e11
M_tierra = 5.95e24
R_tierra = 6.37e6
M_luna = 7.35e22
R_luna = 1.74e6
D_tierra_luna = 384e6
F_tierra_luna = 1.97818857829e+42

#definir funciones

#definir funcion fuerza gravitatoria
def fuerza_grav(M, m, r):
    return G * M * m / r ** 2
#definir funcion distancia
def distancia(M, m, F):
    return sqrt(G * M * m / F)
#definir funcion velocidad de escape
def velocidad_escape(M, R):
    return sqrt(2 * G * M / R)
    
ve_tierra = velocidad_escape(M_tierra, R_tierra)
ve_luna = velocidad_escape(M_luna, R_luna)

#prueba del modulo, no funciona cuando se lo invoca
if __name__ == '__main__':
    print 'Fuerza de atraccion en Newtons entre la Tierra y la Luna es: ', fuerza_grav(M_tierra, M_luna, D_tierra_luna) 
    print 'La distancia entre la tierra y la luna es: ', distancia(M_tierra, M_luna, F_tierra_luna )
    print 'Velocidad de escape de la Tierra: ', velocidad_escape(M_tierra, R_tierra)
    