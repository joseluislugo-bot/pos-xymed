import json
from datetime import datetime

# Catálogo de productos
catalogo = {
    "1": {"nombre": "Semaglutide", "precio": 1200},
    "2": {"nombre": "Tirzepatide", "precio": 1800},
    "3": {"nombre": "Consulta", "precio": 299},
    "4": {"nombre": "Metformina", "precio": 150},
}

carrito = []

# Mostrar menú
def mostrar_catalogo():
    print("\n--- PRODUCTOS ---")
    for clave, producto in catalogo.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']} MXN")

# Agregar al carrito
def agregar_producto(clave):
    if clave in catalogo:
        carrito.append(catalogo[clave])
        print(f"✓ {catalogo[clave]['nombre']} agregado")
    else:
        print("Producto no encontrado")

# Guardar venta
def guardar_venta():
    total = sum(p["precio"] for p in carrito)
    venta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "productos": carrito,
        "total": total
    }
    with open("ventas.json", "a") as archivo:
        archivo.write(json.dumps(venta) + "\n")
    print(f"\n✓ Venta guardada. Total: ${total} MXN")

# Loop principal
print("=== PUNTO DE VENTA XYMED ===")
while True:
    mostrar_catalogo()
    print("\n0. Finalizar venta")
    opcion = input("\nElige producto: ")
    
    if opcion == "0":
        if carrito:
            guardar_venta()
        break
    else:
        agregar_producto(opcion)