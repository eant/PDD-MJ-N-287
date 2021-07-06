import requests
import json
from pprint import pprint

url = 'https://covid-api.mmediagroup.fr/v1/cases'
objeto = json.loads(requests.get(url).text)
paises  = [pais for pais in objeto if pais != 'Global']

mi_seleccion = {}
contador = 1

while True:
   pais_deseado = input("Ingrese el país del que desea obtener los datos (en Ingles): ")
   if pais_deseado not in paises: print("Ese país no está en la lista")
   else:
      url = 'https://covid-api.mmediagroup.fr/v1/cases?country=' + pais_deseado
      objeto = json.loads(requests.get(url).text)
      toda_la_info = objeto['All']
      casos_confirmados = toda_la_info['confirmed']
      fallecidos = toda_la_info['deaths']
      recuperados = toda_la_info['recovered']
      datos_pais = {'país': pais_deseado,
                    'casos confirmados': casos_confirmados,
                    'fallecidos': fallecidos,
                    'recuperados': recuperados}
      
      mi_seleccion['pais' + str(contador)] = datos_pais
      contador += 1
   agregar = input("Desea agregar otro país? s/n: ").upper()
   if agregar == 'N': break
pprint(mi_seleccion)
with open('seleccion_paises.json', 'w') as salida:
   json.dump(mi_seleccion, salida, indent=3, ensure_ascii=False)