print('*** Función sum y next ***')

lista = [1, 2, 3, 4, 5]

# Suma con sum()
resultado = sum(lista)
print(f'Suma de los valores de la lista: {resultado}')

# Suma con valor inicial
resultado = sum(lista, 20)
print(f'Suma con valor inicial: {resultado}')

# La función next
iterador = iter(lista)

print(f'Siguiente elemento del iterable: {next(iterador)}')