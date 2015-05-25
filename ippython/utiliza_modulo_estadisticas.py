# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 06:33:16 2013

@author: daniel
"""
#programa: utiliza_modulo_estadisticas.py

#importa funciones del modulo <estadisticas>
from estadisticas import media, varianza, desviacion_tipica

#data input
notas = []
nota = 0
while (0 <= nota <= 10):
    nota = float(raw_input('Dame una nota (entre 0 y 10): '))
    if 0 <= nota <= 10:
        notas.append(nota)
        
#output
print
print 'Notas: ', notas
print
print 'Media: %16.2f'  %media(notas)
print 'Varianza: %13.2f' %varianza(notas)
print 'Desviacion Tipica: %2.2f' %desviacion_tipica(notas)