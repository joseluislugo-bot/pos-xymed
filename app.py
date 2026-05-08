from flask import Flask, render_template, request, jsonify
import json
import requests
from bs4 import BeautifulSoup 
from datetime import datetime

app = Flask(__name__)

catalogo = {
    "1": {"nombre": "Semaglutide", "precio": 1200},
    "2": {"nombre": "Tirzepatide", "precio": 1800},
    "3": {"nombre": "Consulta", "precio": 299},
    "4": {"nombre": "Metformina", "precio": 150},
}
def obtener_tipo_cambio():
    try:
        url = "https://wise.com/us/currency-converter/usd-to-mxn-rate"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        respuesta = requests.get(url, headers=headers)
        soup = BeautifulSoup(respuesta.text, "html.parser")
        textos = soup.find_all(string=lambda t: "MXN" in str(t))
        for t in textos[:5]:
            texto = t.strip()
            if any(c.isdigit() for c in texto):
                return texto
    except:
        return "No disponible"
@app.route("/")
def index():
    tipo_cambio = obtener_tipo_cambio()
    return render_template("index.html", catalogo=catalogo, tipo_cambio=tipo_cambio)

@app.route("/venta", methods=["POST"])
def guardar_venta():
    datos = request.json
    venta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "productos": datos["productos"],
        "total": datos["total"]
    }
    with open("ventas.json", "a") as f:
        f.write(json.dumps(venta) + "\n")
    return jsonify({"status": "ok", "total": datos["total"]})
@app.route("/historial")
def historial():
    ventas = []
    try:
        with open("ventas.json", "r") as f:
            for linea in f:
                if linea.strip():
                    ventas.append(json.loads(linea))
    except:
        ventas = []
    total_dia = sum(v["total"] for v in ventas)
    return render_template("historial.html", ventas=ventas, total_dia=total_dia)
@app.route("/limpiar", methods=["POST"])
def limpiar_historial():
    open("ventas.json", "w").close()
    return jsonify({"status": "ok"})
if __name__ == "__main__":
    app.run(debug=True)