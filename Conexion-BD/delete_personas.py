# Eliminar registros desde python a mariaDB

import mariadb

# Creamos la conexión
personas_db = mariadb.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (4,)

cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha eliminado a la persona correctamente!')

cursor.close()
personas_db.close()