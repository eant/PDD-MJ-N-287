import requests
import json
from pprint import pprint
import csv

claves = open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves.txt')
lista_claves = [clave.strip('\n') for clave in claves]
key = lista_claves[0]

archivo  = open('sucursales_sol_360.csv')
archivo_csv = csv.reader(archivo, delimiter=';')
ciudades = [linea[0] for linea in archivo_csv]

for ciudad in ciudades:
   url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + ',Argentina&units=metric&lang=es&appid=' + key
   objeto = json.loads(requests.get(url).text)
   #pprint(objeto)
   print("El clima en", ciudad, "es:", objeto['weather'][0]['description'])
