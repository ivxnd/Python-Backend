import mariadb
from dbutils.pooled_db import PooledDB

class Conexion:
    
    DATABASE = 'curso_ibm'
    USERNAME = 'root'
    PASSWORD = 'root'
    DB_PORT = 3306
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None
    
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = PooledDB(
                    creator=mariadb,
                    mincached=1,
                    maxcached=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE
                )
                return cls.pool
            except mariadb.Error as e:
                print(f'Ocurrió un error al crear el pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

# Para probar si crea el pool correctamente
if __name__ == '__main__':
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print('Se ha liberado el objeto conexion1') 