# 🛒 Surtiapp Scraper & Data Analysis
Este proyecto implementa un microservicio de scraping para la tienda **Surtiapp**, desarrollado como parte de una prueba técnica para Iceberg Data.

Permite extraer información estructurada de productos (precio, stock, marca, nombre, imagen, etc) desde cualquier categoría pública del sitio, sin necesidad de autenticarse. El objetivo es apoyar decisiones estratégicas de inventario y precios para mayoristas mediante automatización de datos.

---

## ⚙️ Tecnologías utilizadas
- **Python 3.10+**
- **FastAPI**: Para crear la API RESTful
- **Selenium + Selenium Wire**: Para renderizar contenido dinámico y usar proxy
- **Requests**: Para consumir un endpoint JSON interno con detalles de los productos
- **Pandas**: Para el análisis de los datos

---

## ⚙️ ¿Qué hace este proyecto?
1. Automatiza el scraping de productos por categoría desde Surtiapp usando **Selenium + JSON interno**.
2. Expone un **microservicio API** con FastAPI para solicitar el scraping vía URL.
3. Integra datos históricos y nuevos para realizar análisis exploratorio.
4. Responde preguntas clave del negocio con visualizaciones en **Power BI**.
5. Exporta datasets limpios listos para análisis.

---

## 🚀 ¿Cómo funciona?
### 1. Scraping inteligente
El sitio no muestra el precio de los productos en el HTML. Por eso:
- Se usa **Selenium** para cargar todos los productos visibles de una categoría.
- Se extrae el **Product ID** desde el link de cada producto.
- Luego, se hace una petición a un **endpoint JSON interno** (`/api/ProductDetail/SelectedProduct/{product_id}`) donde están todos los datos sin necesidad de registrarse en la página.

---

### 2. API 
Este proyecto incluye un microservicio creado con FastAPI que permite extraer productos desde una categoría específica de Surtiapp. 

---

## 📊 Análisis de datos
Con el archivo analysis.py se responden 5 preguntas clave del negocio, como:

1. ¿Qué categorías tienen mayor variabilidad de precios?
2. ¿Hay relación entre stock y fluctuaciones de precio?
3. ¿Qué productos fueron añadidos luego del 6 de marzo?
4. ¿Qué patrones muestran los precios por categoría?
5. ¿Qué productos están por agotarse?

Los resultados se guardan en out/ como CSV y fueron visualizados en Power BI en visualizations.pbix. Todos los insights están documentados y listos para decisiones en Surtiapp Scraping Análisis.pdf.

---

## 🚀 ¿Cómo correr el proyecto?
### 1. Clona el repositorio y crea entorno virtual
```bash
git clone https://github.com/TU-USUARIO/Surtiapp-Scraping-Iceberg-Data.git
cd Surtiapp-Scraping-Iceberg-Data
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### 2. Ejecutar la API REST
Corre el microservicio con FastAPI:
```bash
# Asegúrate de estar en tu entorno virtual
uvicorn main:app --reload
```

Luego abre tu navegador en:

👉 http://localhost:8080/docs

Desde ahí puedes probar el endpoint GET /scrapeCategory, pasando la URL de una categoría de Surtiapp. Por ejemplo:
https://tienda.surtiapp.com.co/WithoutLoginB2B/Store/SearchByCategoryResults/Cocina/b1383dff-e904-ea11-add2-501ac5356f6d

Te devolverá una lista de todos los productos y atributos extraídos de esa categoría.

---

## 📁 Estructura del repositorio

```bash
.
├── scraping.py                     # Lógica principal de scraping con Selenium + JSON endpoint
├── main.py                         # FastAPI: define y corre la API del microservicio
├── analysis.py                     # Procesamiento y análisis de los datos extraídos
├── surtiapp_dataset.csv            # Datos históricos
├── data/                           # Carpeta con datasets nuevos obtenidos vía scraping
├── out/                            # Archivos CSV con resultados del análisis por pregunta
├── requirements.txt                # Dependencias necesarias (FastAPI, Selenium, Pandas, etc.)
├── Surtiapp Scraping Análisis.pdf  # Documentación a detalle de los códigos y el análisis obtenido
├── visualizations.pbix             # Visualizaciones creadas con Power BI
└── README.md                       # Este archivo 🙂
