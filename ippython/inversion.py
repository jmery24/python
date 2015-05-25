# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 07:07:30 2013

@author: daniel
"""

# data input
capital = float(raw_input("Capital a invertir en Euros: "))
interes = float(raw_input("Tasa de interes: "))
tiempo = int(raw_input("anios de inversion: "))

if interes > 0:
    calculo = capital*((1+interes/100)**tiempo)
    print "Capital final es de ", calculo
else:
    print "Carece de sentido la inversion"