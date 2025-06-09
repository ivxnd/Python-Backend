print('*** Funciones Lambda ***')

# Sin usar una función lambda
def cuadrado(x):
    return x ** 2

print(f'El cuadrado de 10: {cuadrado(10)}')

# Usando una función lambda
cuadrado_lambda = lambda x : x ** 2

print(f'El cuadrado de 3: {cuadrado_lambda(3)}')

# Con map y lambda
numeros = [1, 2, 3, 4, 5]

# Aplicamos la función lambda para obtener el cuadrado de cada número
cuadrados = list(map(lambda x: x ** 2, numeros))

print(f'Resultado de usar map y lambda: {cuadrados}')

# Con filter y lambda
pares = list(map(lambda x: x % 2 == 0, numeros))

print(f'Resultado de usar filter para números pares: {pares}')