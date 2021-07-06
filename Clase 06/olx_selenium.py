from selenium import webdriver
from bs4 import BeautifulSoup as BS
from time import sleep

#Primero despliego todo el DOM
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\chromedriver.exe')

driver.get('https://www.olx.com.ar/items/q-celular-motorola-E7')

script_js = """
let boton = document.querySelector('[data-aut-id="btnLoadMore"]')
if (boton){
      boton.click()
      }
else{
     return "No existe"
   }  
"""
sleep(3)

while driver.execute_script(script_js) != "No existe": sleep(3)

sleep(3)

#Luego capturo la info deseada
html = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

dom = BS(html, features='html.parser')
productos = dom.find_all(class_="IKo3_")
print("Cantidad de productos:", len(productos))
for producto in productos:
   precio = producto.find(class_="_89yzn").string
   titulo = producto.find(class_="_2tW1I").string
   print(titulo, '-', precio)
