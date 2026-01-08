# Análisis de Clima y Generación Solar

Este proyecto realiza un **análisis conjunto de datos climáticos y generación de energía solar**, utilizando información obtenida desde la **API NASA POWER** y datos de plantas solares reales, con el objetivo de evaluar el comportamiento de la generación frente a variables climáticas.

## Objetivo del proyecto

Analizar cómo variables climáticas como:

- Radiación solar
- Temperatura máxima y mínima
- Nubosidad
- Precipitación

influyen en la **generación de energía de una planta solar**, facilitando la toma de decisiones operativas y de mantenimiento.

---

## Tecnologías utilizadas

- **Python 3**
- **Pandas** – análisis y manipulación de datos
- **NumPy** – cálculos numéricos
- **Matplotlib** – visualización de datos
- **Requests** – consumo de APIs
- **NASA POWER API** – datos climáticos oficiales

---

## Estructura del proyecto

clima-generacion/
│
├── codigo/
│ └── main.py # Script principal de análisis
│
├── API/
│ ├── api.py # Pruebas de consumo de API
│ └── templates/
│ └── index.html # Plantilla HTML
│
├── practica/
│ └── *.py # Ejercicios y pruebas de aprendizaje
│
├── resultados/
│ ├── *.xlsx # Resultados procesados
│ └── *.png # Gráficos generados
│
├── .gitignore
└── README.md

---

## Funcionalidad del script principal

El archivo `codigo/main.py` realiza:

1. Conexión con la **API NASA POWER**
2. Descarga de datos climáticos diarios
3. Limpieza y transformación de datos
4. Generación de gráficos climáticos
5. Exportación de resultados a Excel e imágenes

---

## Resultados obtenidos

- Gráficos de radiación solar diaria
- Análisis de temperatura y precipitación
- Archivos `.xlsx` listos para análisis
- Visualizaciones listas para informes técnicos

Los resultados se almacenan en la carpeta `resultados/`.

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/Cristhian-Velez/clima-generacion.git


# 📁 Estructura del proyecto

