# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:54:57 2013

@author: daniel
"""

# programa: html_479.py
# el programa lee  un file html y sustituye <B> por <I> y lo escribe en
# otro file
# ejercicio 479

#nombre = raw_input('Nombre File: ')
f = open('daniel_mery.html', 'r')

# ambos <while> funcionan
while True: 
#while 1:
    linea = f.readline()
    if linea == '':
        break
    if linea != '':
        print linea    
f.close()