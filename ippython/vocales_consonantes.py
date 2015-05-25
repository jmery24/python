# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 07:16:15 2013

@authand: daniel
"""

#programa: vocales_consonantes.py
#entrado un letra los clasifica como vocal, consonante, mayuscula, minuscula

#data input
letra = raw_input('Entra un solo caracter: ')
print "numero de caracter: ", ord(letra)

#processing and printout
if 'A' > letra > 'Z' and 'a' > letra < 'z':
    print "no es letra"
else:
    if 'A' <= letra <= 'Z' and letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
        print "consonante mayuscula"
    else:
        if 'A' <= letra <= 'Z' and letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            print "vocal mayuscula"
        else:
            if 'a' <= letra <= 'z' and letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
                print "consonante minuscula"
            else:
                if 'a' <= letra <= 'z' and letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                    print "vocal minuscula"
                else:
                    print "no es letra"

print "Gracias por utilizar el programa!!!"
                    
    
        