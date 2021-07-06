import requests
import json
from pprint import pprint

url = 'https://covid-api.mmediagroup.fr/v1/cases?country=Argentina'
objeto = json.loads(requests.get(url).text)
pprint(objeto['All']['confirmed'])