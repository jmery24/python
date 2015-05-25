# programa: diccionarios.py
# son vectores asociativos, funcionan como vectores normales en los que
# los indices pueden ser cualquier objeto inmutable
# numeros, strings y tuplas, cuyos componentes sean inmutables

# creamos el diccionario <tel>
tel = {}

# input
tel['Tigre'] = 1234
tel['Mafalda'] = 3456
tel['Oso'] = 2323

# output
print 'Telefono: ', tel['Mafalda']
print
print 'Miembros del diccionario: ', tel
print
print 'Verificando si es miembros del diccionario con <has_key>'
print 'Tiene telefono: ', tel.has_key('Tigre')
print 'Tiene telefono: ', tel.has_key('Auca')
print 'Miembros del diccionario: ', tel.keys()
print
print 'Verificando si es miembros del diccionario con <get>'
print 'Tiene telefono: ', tel.get('Tigre', 0)
print 'Tiene telefono: ', tel.get('Auca')
print 'Tiene telefono: ', tel.get('Auca', 0)
