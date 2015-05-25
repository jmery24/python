# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 04:42:17 2013

@author: daniel
"""

# programa: file_compara_files_467.py
# programa abre y lee dos ficheros y verifica si el segundo fichero esta
# cifrado del primero 
# ejercicio 467

# input
nombre_uno = raw_input('File primero: ')
nombre_dos = raw_input('File segundo: ')

# abre los dos files a comparar
f_uno = open(nombre_uno, 'r')
f_dos = open(nombre_dos, 'r') 

# lee lineas de ambos files

# en el file segundo aplica codigo de descifrado
for linea in f_dos:
	nueva_linea = ''
	for caracter in linea:
		if caracter >= 'a' and caracter <= 'y':
			nueva_linea += chr(ord(caracter) - 1)
		elif caracter == 'a':
			nueva_linea += 'z'
		else:
			nueva_linea += caracter
	texto_dos = nueva_linea

# en el file primero lee lineas 
for linea in f_uno:
	linea_nueva = ''
	for caracter in linea:
          linea_nueva += caracter
	texto_uno = linea_nueva

# compara ambos textos: el primero y el segundo descifrado  
if texto_uno == texto_dos:
    print '-------------------------------------------------------'
    print 'El file segundo es una version cifrada del file primero'
else:
    print '-------------------------'
    print 'NO es una version cifrada' 

# cierra los files
f_uno.close()
f_dos.close()