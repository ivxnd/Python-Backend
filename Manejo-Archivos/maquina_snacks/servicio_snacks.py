import os.path
from maquina_snacks import Snack

class ServicioSnack:
    NOMBRE_ARCHIVO = './maquina_snacks/snacks.txt'
    
    def __init__(self):
        self.__snacks = []
        
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.__snacks = self.obtener_snack()
        else:
            self.cargar_snacks_iniciales()
    
    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Patatas', 50),
            Snack('Bocadillo', 100),
            Snack('Refresco', 60)
        ]
        
        self.__snacks.extend(snacks_iniciales)
        self.guardar_snacks(snacks_iniciales)
        
    def guardar_snacks(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
                    
        except Exception as e:
            print(f'Error al guardar los snacks en el archivo: {e}')
    
    def obtener_snack(self):
        pass