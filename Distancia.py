import requests
import time

# Tu clave de API de GraphHopper
API_KEY = "e86fdc32-92f1-42e5-a0ed-1f39c4b7ffdb"

# Coordenadas de ciudades
ciudades = {
    "Santiago": "-33.4489,-70.6693",
    "Buenos Aires": "-34.6037,-58.3816"
}

# Opciones de transporte
opciones = {
    "1": "car",
    "2": "bike",
    "3": "foot"
}

def calcular_ruta(origen, destino, transporte):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [origen, destino],
        "vehicle": transporte,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    respuesta = requests.get(url, params=params)
    datos = respuesta.json()

    if 'paths' in datos:
        ruta = datos['paths'][0]
        distancia_km = round(ruta['distance'] / 1000, 2)
        distancia_mi = round(ruta['distance'] / 1609.34, 2)
        duracion_ms = ruta['time']
        duracion_seg = duracion_ms / 1000
        tiempo_legible = time.strftime("%H:%M:%S", time.gmtime(duracion_seg))

        # Resultados
        print("\n--- Resultados del Viaje ---")
        print(f"Ruta: Santiago (Chile) -> Buenos Aires (Argentina)")
        print(f"Medio de transporte: {'A pie' if transporte == 'foot' else 'Bicicleta' if transporte == 'bike' else 'Automóvil'}")
        print(f"Distancia: {distancia_km} km ({distancia_mi} millas)")
        print(f"Duración del viaje: {tiempo_legible}")

        print("\n--- Narrativa del Viaje ---")
        print(f"Tu viaje desde Santiago (Chile) hasta Buenos Aires (Argentina)")
        print(f"- Distancia total: {distancia_km} km ({distancia_mi} millas)")
        print(f"- Duración estimada: {tiempo_legible}")

        print("\nRecomendaciones:")
        print("- Lleva calzado adecuado y protección solar")
        print("- Planifica puntos de abastecimiento")

    else:
        print("❌ Error al obtener la ruta:")
        print(datos)

def main():
    print("***************************************")
    print("*  Calculador de Rutas Chile-Argentina")
    print("*  (Presiona 's' para salir en cualquier")
    print("*   momento)")
    print("***************************************")

    while True:
        ciudad_origen = input("\nCiudad de Origen en Chile: ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ciudad de Destino en Argentina: ")
        if ciudad_destino.lower() == 's':
            break

        print("\nSelecciona medio de transporte:")
        print("1. Automóvil")
        print("2. Bicicleta")
        print("3. A pie")
        opcion = input("Opción (1-3): ")

        if opcion not in opciones:
            print("⚠️ Opción no válida. Intente nuevamente.")
            continue

        calcular_ruta(
            ciudades.get(ciudad_origen, ciudad_origen),
            ciudades.get(ciudad_destino, ciudad_destino),
            opciones[opcion]
        )

    print("Saliendo del programa...")

if __name__ == "__main__":
    main()
