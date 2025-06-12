class Snack:
    contador_snacks = 0
    
    def __init__(self, nombre = '', precio = 0):
        Snack.contador_snacks += 1
        self.__id_snack = Snack.contador_snacks
        self.__nombre = nombre
        self.__precio = precio
    
    def __str__(self):
        return (f'Snack: id_snack = {self.__id_snack}, nombre = {self.__nombre}, '
                f'precio = {self.__precio}')
        
    def escribir_snack(self):
        return f'{self.__id_snack},{self.__nombre},{self.__precio}'
    
    def get_ID(self):
        return self.__id_snack
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    