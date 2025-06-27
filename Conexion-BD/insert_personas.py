# Insertamos registros desde python a mariaDB

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
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
valores = ('Marcos', 'Lopez', 18)

cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Se ha insertado la nueva persona correctamente: {valores}')

cursor.close()
personas_db.close()