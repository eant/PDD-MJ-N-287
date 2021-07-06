import requests

url = 'https://eant.tech/cursos/recursos/peliculas.csv'
respuesta = requests.get(url)
contenido = respuesta.text
with open('pelis.csv', 'w') as pelis:
   pelis.write(contenido)