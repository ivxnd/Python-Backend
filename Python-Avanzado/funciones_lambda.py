print('*** Funciones Lambda ***')

# Sin usar una función lambda
def cuadrado(x):
    return x ** 2

print(f'El cuadrado de 10: {cuadrado(10)}')

# Usando una función lambda
cuadrado_lambda = lambda x : x ** 2

print(f'El cuadrado de 3: {cuadrado_lambda(3)}')