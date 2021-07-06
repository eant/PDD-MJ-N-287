#Usando un argumento de la función open
#archivo = open('frutas.txt', 'r', encoding='utf-8', newline='\r')
archivo = open('frutas.txt', 'r', encoding='utf-8')
for linea in archivo:
   #linea = linea[:-1]
   #linea = linea.strip('\n')
   linea = linea.replace('\n', '')
   print(linea)
   
archivo.close()