import os.path
from maquina_snacks_proyecto.snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = './Manejo-Archivos/maquina_snacks_proyecto/snacks.txt'
    
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
        snacks = []
        
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                
                for linea in archivo:
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
                
        except Exception as e:
            print(f'Error al obtener la lista de snacks: {e}')
            
    def agregar_snacks(self, snack):
        self.__snacks.append(snack)
        self.guardar_snacks([snack])
        
    def mostrar_snacks(self):
        print('--- Snacks en el inventario ---')
        
        for snack in self.__snacks:
            print(snack.__str__())
    
    def get_snacks(self):
        return self.__snacks