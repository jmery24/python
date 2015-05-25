# programa: file_website_open.py
# este programa abre pagina web

# importa funciones de modulo <urllib>
from urllib import *

# input
nombre = raw_input('Website: ')

# abre website
f = urlopen(nombre)
for linea in f:
	print linea[: -1]
f.close()
