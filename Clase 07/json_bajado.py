import json
from pprint import pprint
import requests

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/hospitales/hospitales.geojson'
contenido = requests.get(url).text
objeto = json.loads(contenido)

pprint(objeto)