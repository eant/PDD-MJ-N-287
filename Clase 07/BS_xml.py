from bs4 import BeautifulSoup as BS

archivo = open('books.xml', encoding='utf-8')
xml = BS(archivo, features='lxml')

print(xml.prettify())

fechas = xml.find_all('publishdate')
precios = xml.find_all('price')
for i in range(len(fechas)):
   print("Fecha de publicación:", fechas[i].text)
   print("Precio:", precios[i].text)