import pandas as pd
import obtenerhoras
from datetime import datetime

def calcularfactura(fecha_inicio, fecha_fin):
    tabla = obtenerhoras.obtenerhoras("../archivos/factura.xlsx")

    if("-" in fecha_inicio):
        now = datetime.now()
        fecha_inicio = fecha_inicio.split("-")
        fecha_fin = fecha_fin.split("-")
        f_inicio = str(now.year) + "-" + fecha_inicio[1] + "-" + fecha_inicio[0]
        f_fin = str(now.year) + "-" + fecha_fin[1] + "-" + fecha_fin[0]
    elif("/" in fecha_inicio):
        now = datetime.now()
        fecha_inicio = fecha_inicio.split("/")
        fecha_fin = fecha_fin.split("/")
        f_inicio = str(now.year) + "-" + fecha_inicio[1] + "-" + fecha_inicio[0]
        f_fin = str(now.year) + "-" + fecha_fin[1] + "-" + fecha_fin[0]

    agregar = False
    sumar = []
    for i in range(len(tabla.columns)):
        if(tabla.columns[i] == f_inicio):
            agregar = True
        elif(tabla.columns[i-1] == f_fin):
            agregar = False

        if(agregar):
            sumar.append(tabla.columns[i])

    tabla["Total"] = tabla[sumar].sum(axis=1)
    sumar.insert(0, "Rate")
    sumar.insert(0, "Resource Name")
    sumar.insert(len(sumar), "Total")

    resultado = tabla[sumar]

    return resultado
