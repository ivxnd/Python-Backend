from zona_fit_db.cliente import Cliente
from zona_fit_db.cliente_dao import ClienteDAO

class AppZonaFit:
    
    def __init__(self):
        self.__cliente_dao = ClienteDAO()
    
    def get_clienteDAO(self):
        return self.__cliente_dao
    
    def servicios_clientes(self):
        salir = False
        
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error: {e}')
                
    def mostrar_menu(self):
        print(f'''Menu:
        1. Listar clientes
        2. Agregar cliente
        3. Modificar cliente
        4. Eliminar cliente
        5. Salir''')
        return int(input('Elige una opción: '))
    
    def ejecutar_opcion(self, opcion):
        try:
            if opcion == 1:
                self.listar_clientes()
            if opcion == 2:
                self.agregar_cliente()
            if opcion == 3:
                self.modificar_cliente()
            
            elif opcion == 5:
                return True
            else:
                print('Opción invalida, selecciona una opción del 1 - 5')
        except ValueError:
            print('Solo se aceptan valores numericos')
        except Exception as e:
            print(f'Error: {e}')
            
    def listar_clientes(self):
        try:
            clientes = self.get_clienteDAO().seleccionar()
            print('\n*** Listado de clientes ***')
            for cliente in clientes:
                print(cliente)
            
        except Exception as e:
            print(f'Error al listar clientes: {e}')
            
    def agregar_cliente(self):
        nombre_cliente = input('Introduce el nombre del cliente: ')
        apellido_cliente = input('Introduce el apellido del cliente: ')
        membresia_cliente = int(input('Introduce la membresia del cliente: '))
        nuevo_cliente = Cliente(nombre=nombre_cliente,apellido=apellido_cliente,
                                membresia=membresia_cliente)
        
        try:
            self.get_clienteDAO().insertar(nuevo_cliente)
            print('Cliente agregado correctamente!')
        except Exception as e:
            print(f'Error al agregar el cliente: {e}')
            
    def modificar_cliente(self):
        id_cliente = int(input('Introduce el ID del cliente a actualizar: '))
        nombre_cliente = input('Introduce el nuevo nombre del cliente: ')
        apellido_cliente = input('Introduce el nuevo apellido del cliente: ')
        membresia_cliente = int(input('Introduce la nueva membresia del cliente: '))
        cliente_actualizado = Cliente(id_cliente,nombre_cliente,
                                      apellido_cliente,membresia_cliente)
        
        try:
            self.get_clienteDAO().actualizar(cliente_actualizado)
            print('Cliente actualizado correctamente!')
        except Exception as e:
            print(f'Error al actualizar un cliente: {e}')

# Programa principal
if __name__ == '__main__':
    zona_fit_app = AppZonaFit()
    zona_fit_app.servicios_clientes()