class Pelicula:
    
    def __init__(self, titulo, duracion, fecha_estreno, director):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__fecha_estreno = fecha_estreno
        self.__director = director
    
    # GETTERS
    def get_titulo(self):
        return self.__titulo
    def get_duracion(self):
        return self.__duracion
    def get_fechaEstreno(self):
        return self.__fecha_estreno
    def get_director(self):
        return self.__director
    
    def __str__(self):
        return (f'Pelicula: titulo = {self.get_titulo()}, duracion = {self.get_duracion()}, '
                f'fecha de estreno = {self.get_fechaEstreno()}, director = {self.get_director()}')
    
    def escribir_pelicula(self):
        return f'{self.get_titulo()},{self.get_duracion()},{self.get_fechaEstreno()},{self.get_director()}'