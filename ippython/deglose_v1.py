# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 06:55:00 2013

@author: daniel
"""

#programa:deglose_v1.py
#dada una cantidad de dinero efectuar el deglose en billetes de 500,200,100,50,20,10,5,2,1

#data input
cantidad = int(raw_input('Monto de dinero: '))

#data proccesing and printout
#for deglose in [500,200,100,50,20,10,5,2,1]:
#    print 'Billetes de %d: %d' %(deglose,cantidad/deglose)
#    cantidad = cantidad % deglose

#variante de contador
for deglose in [500,200,100,50,20,10,5,2,1]:
    if cantidad / deglose < 1:
        cantidad = cantidad % deglose
    else:
        print 'Billetes de %3d: %2d' %(deglose,cantidad/deglose)
        cantidad = cantidad % deglose
    