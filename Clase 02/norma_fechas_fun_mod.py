import funciones_norma as fn

fecha = "13/2/2019"
fn.normalizadorFechas(fecha, "%d/%m/%Y")

fecha = "13 days after February 2019"
fn.normalizadorFechas(fecha, '%d days after %B %Y')

fecha = "02/19" #(mes/año)
fn.normalizadorFechas(fecha, '%m/%y', '%m-%Y')

fecha = "13/Febrero/2019"
fn.normalizadorFechas(fn.traductorFecha(fecha), '%d%m%Y')