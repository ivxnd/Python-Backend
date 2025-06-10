print('*** Anexar información en un archivo ***')

nombre_archivo = 'Manejo-Archivos/archivo.txt'

with open(nombre_archivo, 'a') as archivo:
    archivo.write('Anexando informacion...\n')
    archivo.write('Saliendo de anexar informacion...\n')

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())