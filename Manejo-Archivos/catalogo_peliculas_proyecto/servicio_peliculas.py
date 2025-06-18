import os.path
from catalogo_peliculas_proyecto.pelicula import Pelicula

class ServicioPeliculas:
    
    def __init__(self):
        self.__nombre_archivo = './Manejo-Archivos/catalogo_peliculas_proyecto/peliculas.txt'
        
    def get_nombreArchivo(self):
        return self.__nombre_archivo
    
    def guardar_pelicula(self, peliculas):
        try:
            with open(self.get_nombreArchivo(), 'a') as archivo:
                for pelicula in peliculas:
                    archivo.write(f'{pelicula.escribir_pelicula()}\n')       
        except Exception as e:
            print(f'Error al agregar la pelicula: {e}')
            
    def agregar_pelicula(self, pelicula):
        self.guardar_pelicula([pelicula])
    
    def listar_pelicula(self):
        with open(self.get_nombreArchivo(), 'r', encoding='utf8') as archivo:
            print('--- Listado de Películas ---')
            print(archivo.read())
            
    def eliminar_pelicula(self):
        os.remove(self.get_nombreArchivo())
        print(f'Archivo eliminado: {self.get_nombreArchivo()}')
    
    