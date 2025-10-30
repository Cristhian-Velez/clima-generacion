# ============================================================
#  ANÁLISIS DE PLANTA SOLAR - CABEZA Y COLA
# ============================================================

import os
import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1️⃣ DESCARGAR DATOS CLIMÁTICOS DESDE NASA POWER
# ============================================================

# 🔹 URL base corregida
url = "https://power.larc.nasa.gov/api/temporal/daily/point"

params = {
    "start": "20230501",
    "end": "20251021",
    "latitude": 8.7563,
    "longitude": -75.8886,
    "parameters": "ALLSKY_SFC_SW_DWN,T2M_MAX,T2M_MIN,CLOUD_AMT,PRECTOTCORR",
    "format": "JSON",
    "community": "RE"
}

# Petición HTTP con control de errores
try:
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()["properties"]["parameter"]
    df = pd.DataFrame(data)
except Exception as e:
    raise SystemExit(f"❌ Error al descargar datos de NASA POWER: {e}")

# Convertir índice (fecha) a tipo datetime
df.index = pd.to_datetime(df.index)

print(f"📅 Fecha inicial: {df.index.min().strftime('%Y-%m-%d')}")
print(f"📅 Fecha final:   {df.index.max().strftime('%Y-%m-%d')}")

# Crear DataFrame de clima
df_clima = df.copy()
df_clima["Fecha"] = df_clima.index
df_clima.reset_index(drop=True, inplace=True)

# Renombrar columnas
df_clima.rename(columns={
    "ALLSKY_SFC_SW_DWN": "Radiacion_kWhm2",
    "T2M_MAX": "Temp_Max",
    "T2M_MIN": "Temp_Min",
    "CLOUD_AMT": "Nubosidad_%",
    "PRECTOTCORR": "Precipitacion_mm"
}, inplace=True)

print("\n🌦️ Vista previa de datos climáticos:")
print(df_clima.head())

# ============================================================
# 2️⃣ CARGAR DATOS DE GENERACIÓN DESDE EXCEL (ROBUSTO)
# ============================================================

ruta_gen = "datos/SUPERMERCADO_CABEZA_Y_COLA_01052025-21102025.xlsx"

if not os.path.exists(ruta_gen):
    raise FileNotFoundError(f"❌ No se encontró el archivo: {ruta_gen}")

df_gen = pd.read_excel(ruta_gen, skiprows=1)

# Renombrar columnas
df_gen.columns = [
    "Fecha", "Generacion_Wh", "Consumo_Wh",
    "Autoconsumo_Wh", "Inyeccion_Wh", "Importacion_Wh"
]

# Normalización robusta de fechas
if np.issubdtype(df_gen["Fecha"].dtype, np.number):
    df_gen["Fecha"] = pd.to_datetime(df_gen["Fecha"], unit="D", origin="1899-12-30")
else:
    df_gen["Fecha"] = pd.to_datetime(df_gen["Fecha"], dayfirst=True, errors="coerce")

# Eliminar filas sin fecha válida
df_gen = df_gen.dropna(subset=["Fecha"])

# Convertir Wh → kWh
for col in ["Generacion_Wh", "Consumo_Wh", "Autoconsumo_Wh", "Inyeccion_Wh", "Importacion_Wh"]:
    df_gen[col] = pd.to_numeric(df_gen[col], errors="coerce") / 1000.0

# Renombrar columnas finales
df_gen.rename(columns={
    "Generacion_Wh": "Generacion_kWh",
    "Consumo_Wh": "Consumo_kWh",
    "Autoconsumo_Wh": "Autoconsumo_kWh",
    "Inyeccion_Wh": "Inyeccion_kWh",
    "Importacion_Wh": "Importacion_kWh"
}, inplace=True)

# Consolidar por día
df_gen = (
    df_gen.groupby("Fecha", as_index=False)
    .agg({
        "Generacion_kWh": "sum",
        "Consumo_kWh": "sum",
        "Autoconsumo_kWh": "sum",
        "Inyeccion_kWh": "sum",
        "Importacion_kWh": "sum",
    })
)

print("\n⚡ Vista previa de generación (fechas normalizadas):")
print(df_gen.head())

# ============================================================
# 3️⃣ UNIR Y ORDENAR
# ============================================================

df_union = pd.merge(df_gen, df_clima, on="Fecha", how="inner").sort_values("Fecha").reset_index(drop=True)

print("\n🔗 Vista previa del DataFrame unificado:")
print(df_union.head())
print(f"\nTotal de registros combinados: {len(df_union)}")

# ============================================================
# 4️⃣ GRAFICAR RESULTADOS (limpiando valores inválidos)
# ============================================================

df_plot = df_union.replace([-999, -9999, -999.0, -9999.0], np.nan)

# --- Radiación vs Generación ---
plt.figure(figsize=(10, 5))
plt.plot(df_plot["Fecha"], df_plot["Generacion_kWh"], label="Generación (kWh)", color="tab:blue")
plt.plot(df_plot["Fecha"], df_plot["Radiacion_kWhm2"] * 50, "--", label="Radiación (kWh/m²) x50", color="tab:orange")
plt.title("☀️ Radiación solar vs Generación eléctrica - Cabeza y Cola")
plt.xlabel("Fecha")
plt.ylabel("Energía")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()

# --- Nubosidad ---
plt.figure(figsize=(10, 5))
plt.plot(df_plot["Fecha"], df_plot["Nubosidad_%"], color="gray")
plt.title("☁️ Nubosidad diaria - Cabeza y Cola")
plt.xlabel("Fecha")
plt.ylabel("Porcentaje de nubosidad (%)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()

# --- Temperaturas ---
plt.figure(figsize=(10, 5))
plt.plot(df_plot["Fecha"], df_plot["Temp_Max"], "r-", label="Temp. Máx (°C)")
plt.plot(df_plot["Fecha"], df_plot["Temp_Min"], "b-", label="Temp. Mín (°C)")
plt.title("🌡️ Temperaturas diarias - Cabeza y Cola")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()

# --- Precipitación ---
plt.figure(figsize=(10, 5))
plt.bar(df_plot["Fecha"], df_plot["Precipitacion_mm"], color="tab:blue", alpha=0.6)
plt.title("🌧 Precipitación diaria - Cabeza y Cola")
plt.xlabel("Fecha")
plt.ylabel("Precipitación (mm/día)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()

# ============================================================
# 5️⃣ GUARDAR RESULTADO FINAL
# ============================================================

os.makedirs("resultados", exist_ok=True)
ruta_salida = "resultados/Cabeza_y_Cola_Clima_Generacion.xlsx"
df_union.to_excel(ruta_salida, index=False)

print(f"\n✅ Archivo guardado correctamente: {ruta_salida}")


################################################################################################################
#GRAFICAS DE ENERGIA 

#GENERACION TOTAL

plt.figure(figsize=(10,5))
plt.plot(df_union["Fecha"], df_union["Generacion_kWh"], color="tab:green")
plt.title("⚡ Generación diaria - Cabeza y Cola")
plt.xlabel("Fecha")
plt.ylabel("Energía generada (kWh)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

#CONSUMO TOTAL

plt.figure(figsize=(10,5))
plt.plot(df_union["Fecha"], df_union["Consumo_kWh"], color="tab:red", label="Consumo")
plt.plot(df_union["Fecha"], df_union["Generacion_kWh"], color="tab:blue", label="Generación")
plt.title("📊 Generación vs Consumo diario")
plt.xlabel("Fecha")
plt.ylabel("Energía (kWh)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

#AUTOCONSUMO, INYECCIÓN Y IMPORTACIÓN

plt.figure(figsize=(10,6))
plt.stackplot(
    df_union["Fecha"],
    df_union["Autoconsumo_kWh"],
    df_union["Inyeccion_kWh"],
    df_union["Importacion_kWh"],
    labels=["Autoconsumo", "Inyección", "Importación"],
    alpha=0.8
)
plt.title("⚙️ Distribución energética diaria - Cabeza y Cola")
plt.xlabel("Fecha")
plt.ylabel("Energía (kWh)")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

#RADIACIÓN + GENERACIÓN

plt.figure(figsize=(6,5))
plt.scatter(df_union["Radiacion_kWhm2"], df_union["Generacion_kWh"], alpha=0.7, color="tab:orange", edgecolors="k")
plt.title("☀️ Radiación vs Generación (datos reales corregidos)")
plt.xlabel("Radiación (kWh/m²)")
plt.ylabel("Generación (kWh)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

#EVOLUCIÓN GENERAL

df_mensual = df_union.resample("M", on="Fecha").sum(numeric_only=True)
df_mensual[["Generacion_kWh", "Consumo_kWh"]].plot(kind="bar", figsize=(10,5))
plt.title("📆 Generación vs Consumo mensual")
plt.ylabel("kWh")
plt.tight_layout()
plt.show()
