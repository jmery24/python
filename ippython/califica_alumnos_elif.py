# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 07:17:12 2013

@author: daniel
"""

#programa califica_alumnos_elif.py
#Calificacion de examenes de los alumnos

#data input
califica = float(raw_input('califica al alumno <de 0 a 10>: '))

#data processing and printout
if califica < 5:
    print 'Suspenso'
elif 5 <= califica < 7:
    print 'Aprobado'
elif 7 <= califica < 8.5:
    print 'Notable'
elif 8.5 <= califica < 10:
    print 'Sobresaliente'
else:
    print 'Matricula de honor'