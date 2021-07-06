import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base031',
                                   user = 'pdp_usuario031',
                                   password = 'eantpass')
cursor = conexion.cursor()
nombre = 'Gerardo'
apellido = 'Ramírez'
dni = '32659874'
email = 'gerardo@nada.com'
fecha_nac = '2001-08-09'


query = "INSERT INTO alumnos(nombre, apellido, dni, email, fecha_nac) VALUES(%s,%s,%s,%s,%s)"

cursor.execute(query, (nombre, apellido, dni, email, fecha_nac))
conexion.commit()

cursor.close()
conexion.close()