import csv
import mysql.connector
#me contecto a la base
conexion = mysql.connector.connect(host = "cloud.eant.tech", database = "pdp_base031", user = "pdp_usuario031", password = "eantpass")
cursor = conexion.cursor()
#creo la tabla
query ="CREATE TABLE IF NOT EXISTS bares (lon FLOAT NULL,lat FLOAT,id INT NULL,nombre VARCHAR(200) NULL,categoria VARCHAR(200) NULL,cocina VARCHAR (200) NULL,ambientacion VARCHAR(200) NULL,telefono VARCHAR(200) NULL,mail VARCHAR(200) NULL,horario VARCHAR(200) NULL,calle_nombre VARCHAR(200) NULL,calle_altura INT NULL,calle_cruce VARCHAR(200) NULL,direccion_completa VARCHAR(200) NULL,barrio VARCHAR(200) NULL,comuna VARCHAR(100) NULL,codigo_postal VARCHAR(100) NULL,codigo_postal_argentino VARCHAR(100) NULL)"
cursor.execute(query)
#armo la tabla a mandar
with open("oferta_gastronomica.csv") as csv_file:
    file = csv.reader(csv_file)
    next(file)
    values = [tuple(row) for row in file]
    
#inserto la tabla a mandar 
query2 = "INSERT INTO bares (lon, lat, id, nombre, categoria, cocina, ambientacion, telefono, mail, horario, calle_nombre, calle_altura, calle_cruce, direccion_completa, barrio, comuna, codigo_postal, codigo_postal_argentino) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.executemany(query2, values)
conexion.commit()
cursor.close()
conexion.close()