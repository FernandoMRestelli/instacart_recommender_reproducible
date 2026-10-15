# Recomendador Instacart — notebook reproducible

Este repositorio contiene la notebook auditada, sus dependencias directas fijadas y el estudio de Optuna utilizado para seleccionar los hiperparámetros. La copia local también tiene los seis CSV originales y una base DuckDB, que **no se incluyen en Git**.

## Archivos

- `notebooks/01_Tesis_Marketing_Instacart_auditada.ipynb`: pipeline principal; ejecutar las celdas en orden desde la raíz del proyecto o desde `notebooks/`.
- `requirements.txt` y `.python-version`: versiones usadas; Python 3.14.5 en macOS.
- `optuna/optuna_study_temporal_NDCG10_v3.db`: ensayos y mejor configuración de Optuna.
- `data/raw/`: colocar aquí `orders.csv`, `order_products__prior.csv`, `order_products__train.csv`, `products.csv`, `departments.csv` y `aisles.csv`.
- `data/processed/` y `outputs/`: caché DuckDB y resultados que genera la notebook.
- `models/`: la notebook crea `lightgbm_model_auditado.txt` después del entrenamiento.

## Datos

El dataset original es *The Instacart Online Grocery Shopping Dataset 2017*. El [anuncio de Instacart](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2) enlaza una descarga que actualmente devuelve 404. Los seis CSV también figuran en la [página de datos de la competencia de Kaggle](https://www.kaggle.com/c/basket-analysis/data); cada persona debe obtenerlos allí con su propia cuenta y aceptar las reglas aplicables. Los [términos publicados por Instacart](https://gist.github.com/jeremystan/582eba13d6ee27ed465c43dc78934700) prohíben redistribuir el dataset. Por eso los CSV y la base DuckDB están ignorados por Git. No los agregues al repositorio público.

## Cómo ejecutar

```bash
cd instacart-recommender-reproducible
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
mkdir -p data/raw
# Copiar aquí los seis CSV obtenidos de Kaggle: data/raw/
python -m pip install jupyterlab
python -m jupyterlab
```

Abrir `notebooks/01_Tesis_Marketing_Instacart_auditada.ipynb` con el kernel de `.venv` y ejecutar desde la primera celda. La notebook crea `data/processed/instacart.duckdb` si no existe. Conviene disponer de suficiente RAM para el pipeline completo.

El estudio de Optuna incluido conserva 32 ensayos registrados, de los cuales 28 están completos. La notebook carga ese estudio y usa el mejor ensayo disponible; no hace falta repetir la búsqueda para reproducir esa selección. Para hacer una búsqueda nueva, trabajar en otra copia y retirar allí la base de Optuna.

La semilla de la notebook es 42. Las versiones directas están fijadas en `requirements.txt`, pero las dependencias transitivas, el hardware y algunas operaciones paralelas pueden causar pequeñas diferencias numéricas. Se validaron la estructura de la notebook, la carga de los datos y un caso pequeño de predicción y SHAP; **no se ejecutó el entrenamiento completo de esta copia**. Reproducir el estudio completo requiere correrla de principio a fin y comparar las métricas obtenidas.
