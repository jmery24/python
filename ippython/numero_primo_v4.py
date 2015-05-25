# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 07:19:34 2013

@author: daniel
"""

#programa: numero_primo_v4.py
#variante del anterior programa numero_primo_v3 utilizando 
#un bucle <while> y <break>

#data input
num = int(raw_input('Introduce un numero entero: '))
creo_es_primo = True
divisor = 2

#proccesing
while divisor < num:
    if num % divisor == 0:
        creo_es_primo = False
        break
    divisor +=1
    
if creo_es_primo:
    print 'el numero %d es numero primo' %num
else:
    print 'el numero %d  no es numero primo' %num
