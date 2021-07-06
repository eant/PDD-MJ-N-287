from datetime import datetime
            
def normalizadorFechas(fecha, patron_in, patron_out = "%d-%m-%Y"):
   objeto_fecha = datetime.strptime(fecha, patron_in)
   fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
   return fecha_normalizada
   
def traductorFecha(fecha):
   meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO', 'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
   lista = fecha.split(' ')
   dia = lista[0]
   mes = lista[2].upper()
   año = lista[4]
   nro_mes = meses.index(mes) + 1
   fecha_aux = str(dia) + '-' + str(nro_mes)+ '-' + str(año)
   return fecha_aux
   
import csv

with open('reclamos.csv', encoding='iso-8859-1') as archivo_in, open('reclamos_salida.csv', 'w',encoding='utf-8') as archivo_out:
    entrada = csv.reader(archivo_in)
    archivo_out.write('id_cliente,tx_zona,tx_reclamo,fc_reclamo\n')
    for linea in entrada:
        linea = linea[0].split(';')
        fecha = linea[3]
        try:    
            fecha = normalizadorFechas(fecha, "%d-%m-%Y")
            archivo_out.write(linea[0] + ',' + linea[1] + ',' + linea[2] + ',' +fecha + '\n')
        except:
            try:
                fecha = normalizadorFechas(fecha, "%Y-%m-%d")
                archivo_out.write(linea[0] + ',' + linea[1] + ',' + linea[2] + ',' +fecha + '\n')
            except:
                try:
                    fecha = normalizadorFechas(fecha, "%d/%m/%y")
                    archivo_out.write(linea[0] + ',' + linea[1] + ',' + linea[2] + ',' +fecha + '\n')
                except:
                    try:
                        fecha = normalizadorFechas(fecha, "%d/%m/%Y")
                        archivo_out.write(linea[0] + ',' + linea[1] + ',' + linea[2] + ',' +fecha + '\n')
                    except:
                        try:
                            fecha = normalizadorFechas(fecha, "%Y-%d-%m")
                            archivo_out.write(linea[0] + ',' + linea[1] + ',' + linea[2] + ',' +fecha + '\n')
                        except:
                            try:
                                fecha = traductorFecha(fecha)
                                archivo_out.write(linea[0] + ',' + linea[1] + ',' + linea[2] + ',' +fecha + '\n')
                            except:
                                print("")
        
archivo_in.close()
archivo_out.close()
   
