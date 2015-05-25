# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:24:38 2013

@author: daniel
"""

#programa:sumatorio_125.py
#calcula el sumatorio de i**2 utilizando <for in>

#data input
sumatorio = 0
inicial = 2
limite = 0
while inicial > limite:
    inicial = int(raw_input('valor inicial: '))
    if inicial % 2 == 0:
        inicial = inicial
    else:
        inicial = inicial + 1
    limite = int(raw_input('valor limite <mayor o igual que inicial>: '))
    
#proccesing data: variante utilizando for in
limite = limite + 1 #corrige el efecto Obi Wan
for contador in range(inicial,limite,2):
    sumatorio += contador
print 'el valor del sumatorio es: %d' %sumatorio