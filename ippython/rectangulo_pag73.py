# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:12:51 2012

@author: daniel
"""

#Programa: rectangulo_pag73.py
#Proposito: calcula el perimetro y el are de un rectangulo conociendo dos lados
#Autor: Daniel Mery
#Fecha: 12/06/2012

#Input data: valores en metros
altura = float(raw_input("Altura en metros: "))
base = float(raw_input("Base en metros: "))

#Calculo del area y el perimetro
area = altura * base
perimetro = (altura + base) * 2

#printout
print "El perimetro es de: %6.2f metros" % perimetro
print "El area es de: %11.2f metros cuadrados" % area
  