import csv

with open('peliculas.csv', encoding='utf-8') as archivo_in, open('peliculas_salida2.csv', 'w', newline='', encoding='utf-8') as archivo_out:
   entrada = csv.reader(archivo_in)
   salida = csv.writer(archivo_out, delimiter=';')
   salida.writerow(['Director', 'Año', 'Película'])
   for linea in entrada:
      salida.writerow([linea[2], linea[1], linea[0]])