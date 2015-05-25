# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 07:20:26 2013

@author: daniel
"""

# data input
cantidad = float(raw_input("cantidad de Euros: "))

# computation and output data
if cantidad/500 >= 1:
    print "billetes de 500: ", int(cantidad/500)
    cantidad = cantidad%500
else:
    cantidad = cantidad

if cantidad/200 >= 1:
    print "billetes de 200: ", int(cantidad/200)
    cantidad = cantidad%200
else:
    cantidad = cantidad
    
if cantidad/100 >= 1:
    print "billetes de 100: ", int(cantidad/100)
    cantidad = cantidad%100
else:
    cantidad = cantidad
    
if cantidad/50 >= 1:
    print "billetes de 50: ", int(cantidad/50)
    cantidad = cantidad%50
else:
    cantidad = cantidad
    
if cantidad/20 >= 1:
    print "billetes de 20: ", int(cantidad/20)
    cantidad = cantidad%20
else:
    cantidad = cantidad
    
if cantidad/10 >= 1:
    print "billetes de 10: ", int(cantidad/10)
    cantidad = cantidad%10
else:
    cantidad = cantidad
    
if cantidad/5 >= 1:
    print "billetes de 5: ", int(cantidad/5)
    cantidad = cantidad%5
else:
    cantidad = cantidad
    
if cantidad/2 >= 1:
    print "billetes de 2: ", int(cantidad/2)
    cantidad = cantidad%2
else:
    cantidad = cantidad
    
if cantidad/1 >= 1:
    print "billetes de 1: ", int(cantidad/1)
    cantidad = cantidad%1
else:
    cantidad = cantidad  

