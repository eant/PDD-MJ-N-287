import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base031',
                                   user = 'pdp_usuario031',
                                   password = 'eantpass')
cursor = conexion.cursor()

query = '''SELECT id, nombre, apellido, dni
           FROM alumnos
           WHERE nombre IN ("Jorge", "Juan", "René", "Carlos")'''

cursor.execute(query)
alumnos = cursor.fetchall()
for alumno in alumnos:
   print(alumno)


cursor.close()
conexion.close()