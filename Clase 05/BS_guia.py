from bs4 import BeautifulSoup as BS

archivo_html = open('web_ejemplo.html', encoding='utf-8')

dom = BS(archivo_html, features = 'html.parser')

#print(dom.prettify())

#primer_link = dom.a
primer_link = dom.find('a')
print(primer_link.text)

todos_los_links = dom.find_all('a')

print(primer_link['class'])
print(primer_link['href'])

for link in todos_los_links:
   print(link.get('href', "No existe"))
   
historias = dom.find_all(class_ = 'historia')
for historia in historias:
   print(historia.text)

elegido = dom.find(id='link1')

parrafo_historia = dom.find('p', class_='historia')

historia2 = dom.find(attrs={'data-minumero':'124124'})
