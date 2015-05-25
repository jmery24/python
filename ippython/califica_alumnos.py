# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 07:57:16 2013

@author: daniel
"""

#programa califica_alumnos.py
#Calificacion de examenes de los alumnos

#data input
califica = float(raw_input('califica al alumno <de 0 a 10>: '))

#data processing and printout
if califica < 5:
    print 'Suspenso'
else:
    if 5 <= califica < 7:
        print 'Aprobado'
    else:
        if 7 <= califica < 8.5:
            print 'Notable'
        else:
            if 8.5 <= califica < 10:
                print 'Sobresaliente'
            else:
                print 'Matricula de honor'