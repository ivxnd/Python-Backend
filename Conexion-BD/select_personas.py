# Seleccionamos registros desde python a mariaDB

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
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)
    
cursor.close()
personas_db.close()
