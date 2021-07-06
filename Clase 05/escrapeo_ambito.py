from bs4 import BeautifulSoup as BS
import requests
import csv

url = 'https://www.ambito.com/'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html, features='html.parser')

etiquetas_class_title = dom.find_all(class_='title')

n = 0
tabla = [['N°', 'Título', 'Link']]
for etiqueta in etiquetas_class_title:
   etiqueta_target = etiqueta.a
   titulo = etiqueta_target.string
   link = etiqueta_target.get('href', 'No definido')
   n += 1
   print(str(n) + ' / ' + titulo + ' / ' + link)
   fila = [n, titulo, link]
   tabla.append(fila)
   
with open('noticias.csv', 'w', newline='') as file:
   writer = csv.writer(file, delimiter=';')
   writer.writerows(tabla)