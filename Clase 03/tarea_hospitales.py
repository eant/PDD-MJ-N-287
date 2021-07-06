import csv
with open('hospitales.csv',encoding='utf-8') as archivo_in , open('hospitales2.csv','w', newline='',encoding='utf-8') as archivo_out:
    entrada = csv.reader(archivo_in)
    salida = csv.writer(archivo_out)
    next(entrada)
    salida.writerow(['latitude','Longitude','name','label'])
    for linea in entrada:
        print(linea)
        coordenadas = linea[0]
        coordenadas = coordenadas.strip('POINT WK ()')
        coordenadas = coordenadas.split(' ')
        lat = coordenadas[1]
        long = coordenadas[0]
        salida.writerow([lat , long , linea[7] , linea[2]])