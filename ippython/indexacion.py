# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/daniel/.spyder2/.temp.py
"""
#programa:indexacion.py
#varias alternativas

#data input
cadena = raw_input('Escribe una cadena: ')

#recorrido uno
for caracter in cadena:
    print caracter
print 'variante uno ' #espacio en blanco que actua como separador
   
#recorrido dos, utiliza indexacion
for i in range(len(cadena)):
    print i, cadena[i]
print 'variante dos '

#recorrido tres, muestra la cadena en forma inversa
for i in range(len(cadena)):
    print i, cadena[len(cadena)-i-1]
print 'variante inversa '

#recorrido cuatro, muestra cadena en forma inversa
for i in range(len(cadena)-1,-1,-1):
    print i, cadena[i]
print 'nueva variante de inversa'
    

