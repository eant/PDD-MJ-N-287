from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("headless")
options.add_argument("--incognito")
driver = webdriver.Chrome('C:/Users\gonza\Documents\Trabajo\EANT\Python\chromedriver.exe', options=options)

url = 'https://supermercado.carrefour.com.ar/cerveza?_q=cerveza&map=ft'
driver.get(url)

#%%
js_scroll = """
    fondoDePantalla = document.body.scrollHeight      
    for (let i = 0; i < fondoDePantalla; i += 50){
          setInterval(function(){window.scrollTo(0, i)}, 1000);
          }
"""