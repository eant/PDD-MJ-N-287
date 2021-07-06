from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep

#Primero despliego todo el DOM
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\chromedriver.exe')

driver.get('https://www.lanacion.com.ar/')

script_js = """
let fin_de_pantalla = document.body.scrollHeight
window.scrollTo(0, fin_de_pantalla)
return fin_de_pantalla
"""
sleep(3)

pos_actual = 0
pos_siguiente = driver.execute_script(script_js)
sleep(3)

while pos_actual != pos_siguiente:
   pos_siguiente = pos_actual
   pos_actual = driver.execute_script(script_js)
   sleep(3)
   print(pos_actual)
print("Llegamos al final")

#Luego capturo la info deseada
html = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

dom = BS(html, features='html.parser')
articulos  = dom.find_all('h2')
print('Cantidad de articulos: ' + str(len(articulos)))
for articulo in articulos:
    titulo= articulo.text
    vinculo = articulo.a['href']
    print(titulo, '-', vinculo)