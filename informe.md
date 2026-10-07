# Informe Técnico: Análisis de Sensores Industriales y Arquitectura Big Data

---

## 5. Las 5 V aplicadas al proyecto

| V | Explicación | Ejemplo Concreto | ¿CSV Actual o Futura Ampliación? |
| :--- | :--- | :--- | :--- |
| **Volumen** | Cantidad de datos generados y almacenados por el sistema. | Un dataset de 4.4 MiB con 100,000 registros procesados en lote. | **CSV Actual** |
| **Velocidad** | Frecuencia con la que se generan, transmiten y procesan los datos. | Transmisión de datos en tiempo real con lecturas recibidas cada segundo desde miles de sensores. | **Futura Ampliación** |
| **Variedad** | Diversidad de tipos y estructuras de datos ingresando al sistema. | Recepción de imágenes/fotografías térmicas de motores y reportes de mantenimiento en texto libre adjuntos. | **Futura Ampliación** |
| **Veracidad** | Calidad, precisión y nivel de ruido/confiabilidad de los datos recolectados. | Filtro de lecturas erróneas por sensores descalibrados (ej. lecturas nulas o valores fuera de rango). | **Futura Ampliación** |
| **Valor** | Utilidad de negocio que se obtiene al transformar los datos en decisiones. | Generación de una alerta al superar los 85 °C que evita la avería de un motor y ahorra paros de producción. | **CSV Actual** |

---

## 6. Tipos de datos y procesamiento tradicional

### Clasificación de Elementos:
1. **El CSV de sensores:** **Estructurado**. Posee un esquema rígido con filas y columnas bien definidas.
2. **Un mensaje JSON enviado por un sensor:** **Semiestructurado**. Tiene etiquetas y claves-valor flexibles.
3. **Una fotografía de una máquina:** **No estructurado**. Es un archivo binario sin tabla rígida.
4. **El texto libre de un reporte de mantenimiento:** **No estructurado**. Contiene lenguaje natural sin campos estandarizados.

### ¿Por qué 100,000 registros no son Big Data?
Un archivo de 100,000 registros (~4.4 MiB) se procesa en milisegundos en la memoria RAM de cualquier computadora estándar usando scripts sencillos de Python. **No es Big Data** porque no sobrepasa la capacidad de cómputo ni de almacenamiento de un solo nodo.

### Limitaciones al escalar:
* **Desbordamiento de Memoria (RAM):** Cargar archivos masivos (Gigabytes o Terabytes) directamente en RAM causará colapsos (*Out of Memory*).
* **Cuellos de Botella en Disco:** La lectura secuencial de archivos en un solo disco local no soporta miles de eventos por segundo.
* **Procesamiento Mononúcleo:** Python estándar procesa en un solo hilo principal, impidiendo aprovechar cómputo distribuido en paralelo.

---

## 7. Batch y Streaming

### Tipo de Procesamiento Realizado
Se realizó un **procesamiento por lotes (Batch Processing)**, ya que se analizó un conjunto de datos estático, acotado e histórico que ya estaba almacenado previamente en el disco.

### Estrategias de Procesamiento:
1. **Alertas en pocos segundos (> 85 °C):** **Procesamiento en Streaming (Tiempo Real)**. Se procesan los datos evento por evento al momento en que se generan para reaccionar inmediatamente antes de una avería.
2. **Resumen al terminar el día:** **Procesamiento Batch**. Se programa un trabajo nocturno que procesa todo el bloque de datos acumulado en el día para generar reportes directivos.

---

## 8. Arquitecturas Big Data: Lambda y Kappa
