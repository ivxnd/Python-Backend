nombre_archivo = 'Manejo-Archivos/archivo.txt'

# Abrimos el archivo en modo escritura ('w')
with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola\n')
    archivo.write('agregando nueva informacion\n')

print(f'Se ha creado el archivo: {nombre_archivo}')
