# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:55:25 2012

@author: daniel
"""

####Calculo de finanzas

##### Data input
capital = float(raw_input("Capital a invertir: "))
interes = float(raw_input("Tasa de interes %: "))
tiempo = int(raw_input("tiempo en anios de inversion: "))

#### Calculo del capital ganado en este tiempo
dinero = round(capital * (1 + (interes/100)) ** tiempo, 2)

#### Data output
print "El capital final sera: ", dinero, "Euros"
print "Gracias por utilizar este programa"
