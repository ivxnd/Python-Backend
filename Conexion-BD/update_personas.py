# Actualizamos registros desde python a mariaDB

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
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Juan', 'Fernández', 12, 4)

cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la informacion de la persona correctamente!')

cursor.close()
personas_db.close()