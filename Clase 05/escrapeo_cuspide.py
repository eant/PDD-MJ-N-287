from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.cuspide.com/cienmasvendidos'
respuesta = requests.get(url)
respuesta.encoding = 'utf-8'
html = respuesta.text

dom = BS(html, features='html.parser')

articulos  = dom.find_all('article')

for articulo in articulos:
   print(articulo.figure.div.a['title'])

print("Sólo el top 10")
for i in range(len(articulos)):
   print(i+1, articulos[i].figure.div.a['title'])