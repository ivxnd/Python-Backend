print('*** Ordenamiento en Python ***')

# Ordenar una lista
empleados = ['Juan', 'Pedro', 'Maria']
empleados_ordenados = sorted(empleados)

print(f'Empleados ordenados: {empleados_ordenados}')


# Ordenar un diccionario por la llave
empleados_dict = [
    {'nombre': 'Juan', 'salario': 2000},
    {'nombre': 'Maria', 'salario': 3000},
    {'nombre': 'Pedro', 'salario': 2100}
]

empleados_ordenados_salario = sorted(empleados_dict, key=lambda x: x['salario'])

print(f'Empleados ordenados por salario: {empleados_ordenados_salario}')