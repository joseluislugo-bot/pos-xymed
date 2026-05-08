import requests
from bs4 import BeautifulSoup

url = "https://wise.com/us/currency-converter/usd-to-mxn-rate"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
}

respuesta = requests.get(url, headers=headers)
soup = BeautifulSoup(respuesta.text, "html.parser")

print(f"Status: {respuesta.status_code}")
print(f"HTML descargado: {len(respuesta.text)} caracteres")

# Buscar cualquier número que parezca tipo de cambio
textos = soup.find_all(string=lambda t: "MXN" in str(t))
for t in textos[:5]:
    print(t.strip())