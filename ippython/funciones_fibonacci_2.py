# programa: funciones_fibonacci_2.py
# la funcion calcula la serie de fibonacci

#definir funcion <fibonacci>
def fib(num):
    a,b = 0,1
    r = []
    while b < num:
        r.append(b)
        a,b = b,a+b
    return r

# cuerpo del programa
# input
numero = int(raw_input('Introduce un numero: '))

# activa funcion <fibonacci>
print fib(numero)