from maquina_snacks.servicio_snacks import ServicioSnacks

class MaquinaSnacks:
    
    def __init__(self):
        self.__servicio_snacks = ServicioSnacks()
    
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
    