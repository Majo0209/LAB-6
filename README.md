
# 🛠️ Proyecto ETL con Evaluación de Calidad de Datos

Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** para los datasets `customers` y `retail`, con el objetivo de integrar, limpiar y validar datos para la construcción de una tabla de hechos `fact_sales.csv`.  
Además, incluye una evaluación de calidad y la generación de **KPIs y visualizaciones** para apoyar los objetivos de negocio.

---

## 📂 Estructura del Proyecto

```

ETL/
│── data/                       # Archivos de datos
│   ├── customer_data.csv
│   ├── retail_data.csv
│   ├── fact_sales.csv          # Tabla de hechos final
│
│── extract.py                   # Módulo de extracción de datos
│── transform.py                 # Módulo de limpieza y transformaciones
│── main.py                      # Script principal ETL
│── KPI's.ipynb                  # Cálculo de KPIs y visualizaciones
│── qualityEvaluation.ipynb      # Evaluación de calidad de datos
│── EDA.ipynb                    # Análisis exploratorio inicial
│── EDA_Customers.ipynb          # Análisis exploratorio Customers
│── EDA_Retail.ipynb             # Análisis exploratorio Retail
│── requirements.txt             # Dependencias del proyecto
│── README.md                    # Documentación del proyecto

````

---

## ⚙️ Proceso ETL

### 1. **Extract**
- Se cargan los datasets `customer_data.csv` y `retail_data.csv`.

### 2. **Transform**
- Limpieza de datos mediante funciones específicas en `transform.py`:
  - **Teléfonos** estandarizados en formato `+1 (XXX) XXX-XXXX`.
  - **Correos electrónicos** en minúsculas y validados con regex.
  - **Fechas** convertidas a formato estándar `YYYY-MM-DD`.
  - **Edad** restringida al rango 13–120 años.
  - **Montos** (`amount`) numéricos y ≥ 0.
  - **Categorías** validadas contra un catálogo maestro.
  - **Duplicados**:
    - Registros idénticos → eliminados.
    - IDs repetidos con variaciones → se reasigna un identificador único (`1`, `2`, …).
  - Valores inválidos o faltantes → reemplazados por `"No especificado"`.

### 3. **Load**
- Se construye la tabla de hechos `fact_sales.csv`, integrando clientes y transacciones mediante `customer_id`.

---

## 📊 Evaluación de Calidad
En `qualityEvaluation.ipynb` se aplicaron políticas de calidad:
- **Completitud**: todas las columnas críticas alcanzan 100% (con `"No especificado"`).
- **Exactitud**: validaciones de formato y rango.
- **Consistencia**: estandarización de fechas y categorías.
- **Unicidad**: eliminación/corrección de duplicados en `customer_id` y `transaction_id`.
- **Validez**: detección de valores fuera de dominio.

---

## 📈 KPIs y Visualizaciones

### Integridad Financiera
- Total de ventas, promedio por transacción, ventas por vendedor.
- Visualizaciones: barras y distribuciones.

### Planeación Estratégica
- Ventas mensuales, número de transacciones, ticket promedio mensual.
- Visualizaciones: líneas de tiempo.

### Conocimiento de Clientes y Productos
- Ventas por categoría de producto.
- Top 10 clientes.
- Distribución de ventas por género y rango de edad.
- Visualizaciones: barras, donas y histogramas.

### Transparencia en Reportes
- % de completitud por columna.
- Clientes sin contacto.
- Visualizaciones: barras y pie charts.

---

## 🔧 Requerimientos

Instalar dependencias con:

```bash
pip install -r requirements.txt
````

Principales librerías:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`

---

## ▶️ Ejecución

1. Colocar los datasets iniciales en la carpeta `data/`.
2. Ejecutar el pipeline ETL:

```bash
python main.py
```

3. Revisar la tabla final en:

```
data/fact_sales.csv
```

4. Analizar KPIs y calidad en los notebooks `KPI's.ipynb` y `qualityEvaluation.ipynb`.

---

