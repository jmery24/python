# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 06:48:36 2013

@author: daniel
"""

#programa: numero_primo_v3.py
#optimiza el anterior programa numero_primo_v2 utilizando 
#un bucle <while>

#data input
num = int(raw_input('Introduce un numero entero: '))
creo_es_primo = True
divisor = 2

#proccesing
while divisor < num and creo_es_primo:
    if num % divisor == 0:
        creo_es_primo = False   
    divisor +=1
    
if creo_es_primo:
    print 'el numero %d es numero primo' %num
else:
    print 'el numero %d  no es numero primo' %num
