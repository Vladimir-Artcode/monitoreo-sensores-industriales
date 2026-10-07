import csv
from collections import defaultdict
import os

# Rutas relativas requeridas por la rúbrica
RUTA_ENTRADA = os.path.join("data", "sensores_industriales.csv")
RUTA_SALIDA_DIR = "resultados"
RUTA_SALIDA_ALERTAS = os.path.join(RUTA_SALIDA_DIR, "alertas.csv")
UMBRAL_ALERTA = 85.0

def analizar_datos():
    total_registros = 0
    sensores_distintos = set()
    suma_temp_planta = defaultdict(float)
    conteo_temp_planta = defaultdict(int)
    
    temp_maxima = float('-inf')
    lecturas_temp_maxima = []
    
    alertas_totales = 0
    alertas_por_planta = defaultdict(int)
    registros_alerta = []
    
    # Lectura del CSV
    with open(RUTA_ENTRADA, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        encabezados = lector.fieldnames
        
        for fila in lector:
            total_registros += 1
            sensor = fila["id_sensor"]
            planta = fila["planta"]
            temp = float(fila["temperatura_c"])
            
            sensores_distintos.add(sensor)
            suma_temp_planta[planta] += temp
            conteo_temp_planta[planta] += 1
            
            # Evaluación de temperatura máxima (soporta empates)
            if temp > temp_maxima:
                temp_maxima = temp
                lecturas_temp_maxima = [{
                    "id_sensor": sensor,
                    "fecha_hora": fila["fecha_hora"],
                    "planta": planta,
                    "temperatura_c": temp
                }]
            elif temp == temp_maxima:
                lecturas_temp_maxima.append({
                    "id_sensor": sensor,
                    "fecha_hora": fila["fecha_hora"],
                    "planta": planta,
                    "temperatura_c": temp
                })
                
            # Evaluación de alertas (> 85 °C)
            if temp > UMBRAL_ALERTA:
                alertas_totales += 1
                alertas_por_planta[planta] += 1
                registros_alerta.append(fila)

    # Exportar archivo resultados/alertas.csv
    os.makedirs(RUTA_SALIDA_DIR, exist_ok=True)
    with open(RUTA_SALIDA_ALERTAS, mode="w", encoding="utf-8", newline="") as archivo_salida:
        escritor = csv.DictWriter(archivo_salida, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(registros_alerta)

    # Impresión de resultados en consola
    print("==================================================")
    print("      RESULTADOS DEL ANÁLISIS INDUSTRIAL         ")
    print("==================================================")
    print(f"1. Cantidad total de registros: {total_registros:,}")
    print(f"   Cantidad de sensores distintos: {len(sensores_distintos)}")
    print("--------------------------------------------------")
    print("2. Temperatura promedio por planta:")
    for planta, suma in suma_temp_planta.items():
        promedio = suma / conteo_temp_planta[planta]
        print(f"   - {planta}: {promedio:.2f} °C")
    print("--------------------------------------------------")
    print(f"3. Temperatura máxima registrada: {temp_maxima:.2f} °C")
    print("   Ocurrencia(s):")
    for reg in lecturas_temp_maxima:
        print(f"   - Sensor: {reg['id_sensor']} | Fecha/Hora: {reg['fecha_hora']} | Planta: {reg['planta']}")
    print("--------------------------------------------------")
    print(f"4. Total de lecturas con alerta (> {UMBRAL_ALERTA} °C): {alertas_totales:,}")
    print("--------------------------------------------------")
    
    # Planta con más alertas (soporta empates)
    if alertas_por_planta:
        max_alertas = max(alertas_por_planta.values())
        plantas_top = [p for p, c in alertas_por_planta.items() if c == max_alertas]
        print(f"5. Planta(s) con más alertas ({max_alertas} alertas):")
        for p in plantas_top:
            print(f"   - {p}")
    else:
        print("5. No se registraron alertas.")
    print("==================================================")
    print(f"Archivo de alertas generado en: {RUTA_SALIDA_ALERTAS}")

if __name__ == "__main__":
    analizar_datos()
