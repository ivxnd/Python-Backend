nombres = ['Pepe', 'Marta', 'Juan']
edades = [19, 30, 32]
ciudades = ['Granada', 'Valencia', 'Málaga']

# Combinamos las listas usando la función zip
personas = zip(nombres, edades, ciudades)

# Iteramos sobre el resultado
for persona in personas:
    print(persona)