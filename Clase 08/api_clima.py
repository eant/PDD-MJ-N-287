import requests
import json
from pprint import pprint

claves = open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves.txt')
lista_claves = [clave.strip('\n') for clave in claves]
key = lista_claves[0]

ciudad = 'San Juan, Argentina'

ciudad_cod = requests.utils.quote(ciudad)

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&units=metric&lang=es&appid=' + key

objeto = json.loads(requests.get(url).text)

#pprint(objeto)
print("El clima en", ciudad, "es:", objeto['weather'][0]['description'])
