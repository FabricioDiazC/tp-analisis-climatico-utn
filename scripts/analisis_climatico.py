# analisis_climatico.py
# Descripción: Script de análisis de anomalías de temperatura global.
# Dataset: GISTEMP / GCAG – DataHub.io
# Autor: P2 - Desarrollador Técnico (Paco)
# Cátedra: Organización Empresarial – UTN TUP 2026

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carga de datos desde URL pública
URL = "https://datahub.io/core/global-temp/r/annual.csv"
df = pd.read_csv(URL)
df = df[df["Source"] == "GISTEMP"].copy()
df.rename(columns={"Year": "anio", "Mean": "anomalia_temp"}, inplace=True)
df.dropna(subset=["anomalia_temp"], inplace=True)
df.sort_values("anio", inplace=True)

# Indicadores estadísticos
print(f"Anomalía promedio : {df['anomalia_temp'].mean():+.4f} C")
print(f"Anomalía máxima   : {df['anomalia_temp'].max():+.4f} C")
print(f"Anomalía mínima   : {df['anomalia_temp'].min():+.4f} C")

# Exportación de resultados
df.to_csv("datos/temperatura_global_procesada.csv", index=False)
print("Archivos exportados correctamente.")
