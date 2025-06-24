from catalogo_peliculas_proyecto.servicio_peliculas import ServicioPeliculas
from catalogo_peliculas_proyecto.pelicula import Pelicula

class CatalogoPeliculas:
    
    def __init__(self):
        self.__servicio_peliculas = ServicioPeliculas()
        
    def get_servicioPeliculas(self):
        return self.__servicio_peliculas
    def get_peliculas(self):
        return self.__peliculas
    
    def catalogo_peliculas(self):
        salir = False
        
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error: {e}')
    
    def mostrar_menu(self):
        print(f'''Menu:
        1. Agregar pelicula
        2. Listar peliculas
        3. Eliminar catalogo
        4. Salir''')
        return int(input('Elige una opción: '))
    
    def ejecutar_opcion(self, opcion):
        try:
            if opcion == 1:
                self.agregar_pelicula()
            elif opcion == 2:
                self.listar_peliculas()
            elif opcion == 3:
                self.eliminar_catalogo()
            elif opcion == 4:
                return True
            else:
                print('Opción invalida, selecciona una opción del 1 - 4')
        except ValueError:
            print('Solo se aceptan valores numericos')
        except Exception as e:
            print(f'Error: {e}')
    
    def agregar_pelicula(self):
                
        titulo_pelicula = input('Introduce el titulo de la pelicula: ')
        duracion_pelicula = int(input('Introduce la duracion de la pelicula (minutos): '))
        fecha = input('Introduce la fecha de estreno: ')
        director = input('Introduce el nombre del director: ')
        nueva_pelicula = Pelicula(titulo_pelicula, duracion_pelicula, fecha, director)
        
        try:
            self.get_servicioPeliculas().agregar_pelicula(nueva_pelicula)
            print('Se ha agregado la pelicula correctamente!')
        except Exception as e:
            print(f'Error al agregar la pelicula')
    
    def listar_peliculas(self):
        try:
            self.get_servicioPeliculas().listar_pelicula()
        except Exception as e:
            print(f'Error al leer las peliculas: {e}')
    
    def eliminar_catalogo(self):
        try:
            self.get_servicioPeliculas().eliminar_pelicula()
        except Exception as e:
            print(f'Error al borrar el catalogo: {e}')

# Programa principal
if __name__ == '__main__':
    catalogo_peliculas_app = CatalogoPeliculas()
    catalogo_peliculas_app.catalogo_peliculas()
    
        
        
        