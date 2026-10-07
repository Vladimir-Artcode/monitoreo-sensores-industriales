# Sistema de Monitoreo de Sensores Industriales

## Objetivo del Proyecto
Analizar un conjunto de datos simulados de 100,000 lecturas de temperatura y vibración provenientes de sensores instalados en cuatro plantas industriales, identificar anomalías térmicas y exportar reportes de alertas para soporte en el mantenimiento predictivo.

> **Nota:** Los datos analizados en este proyecto (`data/sensores_industriales.csv`) son **completamente simulados** con fines didácticos.

---

## Descripción de los Datos
El dataset principal `data/sensores_industriales.csv` contiene las siguientes columnas:

| Columna | Significado |
| :--- | :--- |
| `id_registro` | Identificador único de la lectura |
| `fecha_hora` | Estampa de tiempo (timestamp) de la lectura |
| `id_sensor` | Identificador único del sensor |
| `planta` | Planta industrial de origen |
| `temperatura_c` | Temperatura registrada en grados Celsius (°C) |
| `vibracion_mm_s` | Nivel de vibración en milímetros por segundo (mm/s) |

---

## Requisitos e Instalación

Este proyecto fue desarrollado utilizando exclusivamente la **biblioteca estándar de Python (Python 3.8+)**, por lo que **no requiere la instalación de librerías externas de terceros**.

### Instrucciones de Ejecución

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Vladimir-Artcode/monitoreo-sensores-industriales.git](https://github.com/Vladimir-Artcode/monitoreo-sensores-industriales.git)
   cd monitoreo-sensores-industriales
