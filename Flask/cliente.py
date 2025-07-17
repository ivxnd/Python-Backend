class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__membresia = membresia
        
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_membresia(self):
        return self.__membresia
    
    def __str__(self):
        return (f'Id: {self.get_id()}, Nombre: {self.get_nombre()}, '
               f'Apellido: {self.get_apellido()}, Membresia: {self.get_membresia()}')