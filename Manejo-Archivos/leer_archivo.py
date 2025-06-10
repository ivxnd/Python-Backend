print('*** Leer archivos en Python ***')

nombre_archivo = 'Manejo-Archivos/archivo.txt'

# Con el método readlines()
with open(nombre_archivo, 'r') as archivo:
    # Leemos todas las lineas del archivo
    lineas = archivo.readlines()
    
    for linea in lineas:
        print(linea.strip())
        
# Con el método read()
print('\nLeyendo el contenido con el método read')

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())