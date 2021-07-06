import csv

archivo_in = open('peliculas.csv', encoding='utf-8')
tabla = csv.reader(archivo_in)
archivo_out = open('peliculas_salida.csv', 'w', encoding='utf-8')

for linea in tabla:
   #print(linea)
   unidos = ','.join([linea[2], linea[1], linea[0]])
   archivo_out.write(unidos + '\n')

archivo_in.close()
archivo_out.close()