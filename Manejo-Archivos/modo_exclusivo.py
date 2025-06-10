print('*** Abrir un archivo en modo exclusivo ***')

nombre_archivo = 'Manejo-Archivos/archivo.txt'

try: 
    with open(nombre_archivo, 'x') as archivo:
        archivo.write('Escritura en modo exclusivo\n')
        archivo.write('agregando nueva informacion\n')
        
    print(f'Se ha creado el archivo: {archivo}')
except FileExistsError:
    print(f'El archivo {nombre_archivo} ya existe.')