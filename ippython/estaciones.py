# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:55:21 2013

@author: daniel
"""

#program:estaciones.py

#data input
mes = int(raw_input('Numero de Mes <1 to 12>: '))

#processing
if 1 <= mes <= 3:
    print 'Invierno'
else:
    if mes == 4 or mes == 5 or mes == 6:
        print 'Primavera'
    else:
        if not(mes < 7 or mes > 9):
            print 'Verano'
        else:
            if not(mes != 10 and mes != 11 and mes != 12):
                print 'Otonio'
            else:
                print 'Ningun anio tiene %d meses ' %mes
        