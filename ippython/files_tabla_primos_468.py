# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 05:33:28 2013

@author: daniel
"""

# programa: files_tabla_primos_468.py
# abre el fichero <primos.txt> y escribe los numeros primos
# comprendidos en [1 100]

# abre el fichero
primos = open('primos.txt', 'w')

# calcula los cien primeros numeros primos
for i in range(2, 101):
    contador = 0
#    creo_es_primo = True
    for k in range(2, i):
        if i % k == 0:
            contador += 1
#            creo_es_primo = False            
#            break
    if contador == 0:    
#    if creo_es_primo:
        print 'numero primo: ', i
        primos.write(str(i) + '\n')
primos.close()
# si activamos lineas: (18,22,23,25) y desactivamos lineas (17,21,24) 
# funciona tambien el programa