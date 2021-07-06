import funciones_norma as fn

fecha = "13 February 2019"
try:
   fn.normalizadorFechas(fecha, '%d days after %B %Y')
   print("Método 1")
except:
   try:
      fn.normalizadorFechas(fecha, '%d days %B %Y')
      print("Método 2")
   except:
      print("No funcionó")