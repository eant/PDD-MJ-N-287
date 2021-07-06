from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

estudiante = {'nombre': 'Gonzalo', 'apellido': 'García'}

#cliente.universidad.alumnos.insert_one(estudiante)

bd = cliente['universidad']

coleccion = bd['alumnos']

estudiantes = [{'nombre': 'Pedro', 'apellido': 'Ramone'},
               {'nombre': 'Edgardo', 'apellido': 'Cuevas', 'dni': 45125369},
               {'nombre': 'Alicia', 'apellido': 'Jimenez', 'hijos':[{'nombre': 'Juan', 'edad': 12}, {'nombre': 'Jimena', 'edad': 8}]}
   ]
coleccion.insert_many(estudiantes)
print("Datos subidos")