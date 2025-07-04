from zona_fit_db.conexion import Conexion
from zona_fit_db.cliente import Cliente

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'
    
    @classmethod
    def seleccionar(cls):
        conexion = None
        
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            
            # Mapeo de clase-tabla cliente
            clientes = []
            
            for registro in registros:
                cliente = Cliente(registro[0],registro[1]
                                  ,registro[2],registro[3])
                clientes.append(cliente)
                
            return clientes
        except Exception as e:
            print(f'Error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.get_nombre(), cliente.get_apellido(), cliente.get_membresia())
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            
            return cursor.rowcount
        except Exception as e:
            print(f'Error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.get_nombre(), cliente.get_apellido(), 
                       cliente.get_membresia(), cliente.get_id())
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            
            return cursor.rowcount()
        except Exception as e:
            print(f'Error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
if __name__ == '__main__':
    # Insertar cliente
    #cliente1 = Cliente(nombre='Marta', apellido='Fernández', membresia=300)
    #clientes_insertados = ClienteDAO.insertar(cliente1)
    #print(f'Clientes insertados: {clientes_insertados}')
    
    # Actualizar cliente
    cliente_actualizado = Cliente(3, 'Alma', 'Pérez', 400)
    ClienteDAO.actualizar(cliente_actualizado)
    print(f'Cliente actualizado: {cliente_actualizado}')
    
    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    
    for cliente in clientes:
        print(cliente)