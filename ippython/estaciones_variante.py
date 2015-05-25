# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:17:51 2013

@author: daniel
"""

#program:estaciones_variante.py

#data input
mes = int(raw_input('Numero de Mes <1 to 12>: '))

#processing and printout
if 1 <= mes <= 3:
        print 'Invierno'
else:
    if 4 <= mes <=6:
        print 'Primavera'
    else:
        if 7 <= mes <= 9:
            print 'Verano'
        else:
            if 10 <= mes <= 12:
                print 'Otonio'
            else:
                if mes < 0:
                    print 'No existen anios negativos'
                else:
                    print 'Ningun anio tiene %d meses ' %mes