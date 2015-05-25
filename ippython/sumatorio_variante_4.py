# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 07:55:33 2013

@author: daniel
"""

#programa:sumatorio_variante_4.py
#calcula el sumatorio de i utilizando for in

#data input
sum = 0
i = 2
lim = 0
while i > lim:
    i = int(raw_input('valor de i: '))
    lim = int(raw_input('valor de limite mayor o igual que <i>: '))
    
#proccesing data: variante utilizando for in
lim = lim + 1 #corrige el efecto Obi Wan
for contador in range(i,lim):
    sum += contador
print 'el valor del sumatorio es %i ' %sum