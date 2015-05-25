## programa: string_len.py
# definicion de <string> (dato compuesto) y longitud del string <len>

## definicion

# definicion: tipo de dato compuesto
print '*--------------------------------------------------------------*'
print '|Un string se compone de caracteres, que son sus piezas menores|'
print '|o unidades. Por esta razon a un string se le define como un   |'
print '|dato compuesto.                                               |'
print  
print '|a un tipo de dato compuesto <string> lo podemos porcesar como |'
print '|un unico elemento o acceder a sus partes <caracteres>.        |'
print
print '|El numero entre corchetes es el indice, o sea, nos indica la  |'
print '|posicion del caracter que deseamos acceder.                   |'
print '*--------------------------------------------------------------*'
print
# definicion de <len>, longitud de una cadena
print '*--------------------------------------------------------------*'
print '|La funcion longitud <len> devuelve la cantidad de caracteres  |'
print '|de una cadena <string>                                        |'
print '*--------------------------------------------------------------*'
print

## ejemplos

# dato compuesto
fruta = 'banana'
letra = fruta[0]
print 'fruta = "banana": ', fruta
print 'letra = fruta[0]: ', letra
print '"banana"[2]: ', 'banana'[2]
print 

# longitud <len>
print 'len(fruta): ', len(fruta)
print 'len("banana"): ', len('banana')
print 'len(fruta[0]): ', len(fruta[0])
print 'len("banana"[3]): ', len('banana'[3])
