from maquina_snacks.servicio_snacks import ServicioSnacks
from maquina_snacks.snack import Snack

class MaquinaSnacks:
    
    def __init__(self):
        self.__servicio_snacks = ServicioSnacks()
        self.productos = []
    
    def maquina_snacks(self):
        salir = False
        
        print('*** Maquina de Snacks ***')
        self.__servicio_snacks.mostrar_snacks()
        
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error: {e}')
    
    def mostrar_menu(self):
        print(f''' Menu: 
              1. Comprar Snack
              2. Mostrar ticket
              3. Agregar Nuevo Snack al Inventario
              4. Mostrar Inventario Snacks
              5. Salir ''')
        return int(input('Elige una opción: '))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.__servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            return True
        else:
            print('Opción invalida, selecciona una opción del 1 - 5')
        return False
    
    def comprar_snack(self):
        
        id_snack = int(input('Introduce el ID del snack a comprar: '))
        snacks = self.__servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Id snack no encontrado: {id_snack}')
            
    def mostrar_ticket(self):
        
        if not self.productos:
            print('Lista de productos vacía')
            return
        total = sum(snack.precio for snack in self.productos)
        print('--- Ticket de Venta ---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')
        
    def agregar_snack(self):
        
        nombre_snack = input('Introduce el nombre del snack: ')
        precio = float(input('Introduce el precio del snack: '))
        nuevo_snack = Snack(nombre_snack, precio)
        
        try:
            self.__servicio_snacks.agregar_snacks(nuevo_snack)
            print('Se ha agregado el snack correctamente!')
        except Exception as e:
            print(f'Error al agregar el snack: {e}')
            
# Programa principal
if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()
    