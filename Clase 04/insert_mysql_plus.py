import mysql.connector

conexion = mysql.connector.connect(host = 'cloud.eant.tech',
                                   database = 'pdp_base031',
                                   user = 'pdp_usuario031',
                                   password = 'eantpass')
cursor = conexion.cursor()
cursor.execute("SELECT dni FROM alumnos")
lista_dnis = [dni[0] for dni in cursor]

continuar = 's'
while continuar == 's':
    dni=input('Ingrese DNI: ')
    if int(dni) in lista_dnis: print("Este dni ya fue ingresado")
    else:
       lista_dnis.append(int(dni))
       nombre= input('Ingrese nombre: ')
       apellido= input('Ingrese apellido: ')
       email= input('Ingrese Correo: ')
       fecha_nac= input('Ingrese fecha de nacimiento (AAAA-MM-DD): ')
       cursor = conexion.cursor()
       query = "INSERT INTO alumnos(nombre, apellido, dni, email, fecha_nac) VALUES(%s, %s, %s, %s, %s)"
       cursor.execute(query, (nombre, apellido, dni, email, fecha_nac))
       continuar= input('Desea continuar s o n: ')

conexion.commit()
cursor.close()
conexion.close()