import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import io


class Actividad3:
    def __init__(self, ruta_resultados="Resultados_actividad_3/"):
        self.ruta_resultados = ruta_resultados
        self._crear_directorio()  # Asegura que la carpeta exista

    def _crear_directorio(self):
        """Crea el directorio si no existe"""
        if not os.path.exists(self.ruta_resultados):
            os.makedirs(self.ruta_resultados)

    def guardar_resultados(self, contenido, nombre_archivo):
        """Guarda los resultados en un archivo dentro de la carpeta correcta"""
        ruta_completa = os.path.join(self.ruta_resultados, nombre_archivo)
        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"Archivo guardado en: {ruta_completa}")

# 🔹 Crear instancia de la clase
actividad = Actividad3()

# 🔹 Punto 1: DataFrame simple
df = pd.DataFrame({'Granadillas': [20], 'Tomates': [50]})

# 🔹 Punto 2: DataFrame con índices personalizados
ventas_frutas = pd.DataFrame({'Granadillas': [20, 49], 'Tomates': [50, 100]},  
                             index=['Ventas 2021', 'Ventas 2022'])

# 🔹 Punto 3: Serie de utensilios
utensilios = pd.Series({'Cuchara': '3 unidades',  
                        'Tenedor': '2 unidades',  
                        'Cuchillo': '4 unidades',  
                        'Plato': '5 unidades'},  
                        name='cocina')

# 🔹 Punto 4: Gráfico de barras

archivo_vinos = "Resultados_actividad_3/Archivo_kaggle_descargado/winemag-data_first150k.csv" 

# 🔹 Punto 5: Descarga dataset wine review

if os.path.exists(archivo_vinos):
    review = pd.read_csv(archivo_vinos)
    contenido_review = "\n" + review.head(5).to_csv(index=False)  # Guardamos solo las primeras 5 filas para no hacer el CSV gigante
else:
    contenido_review = "Error: Archivo de vinos no encontrado.\n"

# 🔹 Punto 6: Informacion del DataFrame

if os.path.exists(archivo_vinos):
    buffer = io.StringIO()
    review.info(buf=buffer)
    info_review = buffer.getvalue()
else:
    info_review = "Error: No se pudo obtener la información del DataFrame porque el archivo no existe.\n"

# 🔹 Punto 7: Calcular el precio promedio
if os.path.exists(archivo_vinos) and 'price' in review.columns:
    precio_promedio = review['price'].mean()
    resultado_precio_promedio = f"El precio promedio del vino es: {precio_promedio:.2f}\n"
else:
    resultado_precio_promedio = "Error: No se pudo calcular el precio promedio. La columna 'price' no existe o el archivo no está disponible.\n"


# 🔹 Ejercicio 8: Calcular el precio más alto pagado
if os.path.exists(archivo_vinos) and 'price' in review.columns:
    precio_maximo = review['price'].max()
    resultado_precio_maximo = f"El precio más alto pagado por un vino es: {precio_maximo:.2f}\n"
else:
    resultado_precio_maximo = "Error: No se pudo determinar el precio más alto. La columna 'price' no existe o el archivo no está disponible.\n"

# 🔹 Ejercicio 9: Filtrar todos los vinos de California
if os.path.exists(archivo_vinos) and 'province' in review.columns:
    vinos_california = review[review['province'] == 'California']
    resultado_vinos_california = f"Número de vinos de California: {len(vinos_california)}\n"
    resultado_vinos_california += vinos_california.head(10).to_csv(index=False)  # Guardamos solo las primeras 5 filas para visualización
else:
    resultado_vinos_california = "Error: No se pudo filtrar los vinos de California. La columna 'province' no existe o el archivo no está disponible.\n"


# 🔹 Ejercicio 10: Encontrar el vino con el precio más alto
if os.path.exists(archivo_vinos) and 'price' in review.columns:
    idx_max_price = review['price'].idxmax()
    vino_mas_caro = review.loc[idx_max_price].to_string()
    resultado_vino_mas_caro = f"Información del vino más caro:\n{vino_mas_caro}\n"
else:
    resultado_vino_mas_caro = "Error: No se pudo obtener la información del vino más caro. La columna 'price' no existe o el archivo no está disponible.\n"

# 🔹 Ejercicio 11: Tipos de uva más comunes en California
if os.path.exists(archivo_vinos) and 'variety' in review.columns:
    variedades_comunes = vinos_california['variety'].value_counts().head(15)
    resultado_variedades_comunes = "Tipos de uva más comunes en California:\n" + variedades_comunes.to_string() + "\n"
else:
    resultado_variedades_comunes = "Error: No se pudo determinar los tipos de uva más comunes. La columna 'variety' no existe o el archivo no está disponible.\n"

# 🔹 Ejercicio 12: Top 10 tipos de uva más comunes en California
if os.path.exists(archivo_vinos) and 'variety' in review.columns:
    top_10_variedades = vinos_california['variety'].value_counts().head(10)
    resultado_top_10_variedades = "Top 10 tipos de uva más comunes en California:\n" + top_10_variedades.to_string() + "\n"
else:
    resultado_top_10_variedades = "Error: No se pudo determinar los 10 tipos de uva más comunes. La columna 'variety' no existe o el archivo no está disponible.\n"


# 🔹 Preparar contenido para el CSV
contenido_csv = "### Ejercicio 1: DataFrame Simple\n"
contenido_csv += df.to_csv(index=False)
contenido_csv += "\n### Ejercicio 2: Ventas de Frutas\n"
contenido_csv += ventas_frutas.to_csv()
contenido_csv += "\n### Ejercicio 3: Utensilios de Cocina\n"
contenido_csv += utensilios.to_csv(header=True)
contenido_csv += "\n### Ejercicio 4: Se descarga archivo Wine Reviews - winemag-data-130k-v2.csv\n"
contenido_csv += "\n### Ejercicio 5: Wine Reviews (Primeras 5 filas)\n"
contenido_csv += contenido_review
contenido_csv += "\n### Ejercicio 6: Información del DataFrame (Wine Reviews)\n"
contenido_csv += info_review
contenido_csv += "\n### Ejercicio 7: Precio Promedio del Vino\n"
contenido_csv += resultado_precio_promedio
contenido_csv += "\n### Ejercicio 8: Precio Más Alto Pagado por un Vino\n"
contenido_csv += resultado_precio_maximo
contenido_csv += "\n### Ejercicio 9: Vinos de California\n"
contenido_csv += resultado_vinos_california
contenido_csv += "\n### Ejercicio 10: Información del Vino Más Caro\n"
contenido_csv += resultado_vino_mas_caro
contenido_csv += "\n### Ejercicio 11: Tipos de Uva Más Comunes en California\n"
contenido_csv += resultado_variedades_comunes
contenido_csv += "\n### Ejercicio 12: Top 10 Tipos de Uva Más Comunes en California\n"
contenido_csv += resultado_top_10_variedades


# 🔹 Guardar en la carpeta correcta
actividad.guardar_resultados(contenido_csv, "resultados_actividad_3.csv")