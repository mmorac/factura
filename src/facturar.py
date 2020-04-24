import calcularfactura
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/factura")

def factura():
    tabla = calcularfactura.calcularfactura("27-03", "24-04")
    codigo = pd.DataFrame.to_html(tabla)
    return render_template("factura.html", codigo = codigo)
