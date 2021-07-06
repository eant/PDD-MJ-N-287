from pprint import pprint
import json

#Variable
x = 0
#Lista
lista = []
#Tupla
tupla = ()
#Diccionario
diccionario = {}

edad = 5
le_gusta = ['Comer', 'Correr a las palomas', 'ladrar de noche']
perro = {'nombre': 'Rocco',
         'tipo': 'perro',
         'raza': 'Labrador'
         }

#Combinación
perro.update({'edad': edad})
perro.update({'le_gusta': le_gusta})

#pprint(perro)

#Nuevo objeto amo
amo = {'nombre': 'Roberto',
       'tipo': 'Humano',
       'le_gusta': ['Una buena conversación', 'los animales', 'Un buen partido de fútbol'],
       'edad': 45,
       'mascota': perro
       }
#pprint(amo)
objeto = {'amo':amo}
with open('amo.json', 'w') as archivo_json:
   json.dump(objeto, archivo_json, indent=3, ensure_ascii=False)   


