# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:42:42 2013

@author: daniel
"""

#program:estaciones_variante_1.py

#data input
mes = int(raw_input('Numero de Mes <1 to 12>: '))

#processing and printout
if mes == 1 or mes == 2 or mes == 3:
        print 'Invierno'
else:
    if mes ==4 or mes == 5 or mes == 6:
        print 'Primavera'
    else:
        if mes == 7 or mes == 8 or mes == 9:
            print 'Verano'
        else:
            if mes == 10 or mes ==11 or mes == 12:
                print 'Otonio'
            else:
                if mes < 0:
                    print 'No existen anios negativos'
                else:
                    print 'Ningun anio tiene %d meses ' %mes