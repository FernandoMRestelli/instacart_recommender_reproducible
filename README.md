# Recomendador Instacart — notebook reproducible

Este repositorio contiene la notebook auditada, sus dependencias directas fijadas y el estudio de Optuna utilizado para seleccionar los hiperparámetros.

## Datos

El dataset original es *The Instacart Online Grocery Shopping Dataset 2017*. Descargá los seis CSV desde [Instacart Market Basket Analysis en Kaggle](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis), descomprimilos y colocalos en `data/raw/`:

- `orders.csv`

- `order_products__prior.csv`

- `order_products__train.csv`

- `products.csv`

- `departments.csv`

- `aisles.csv`

Los datos no se incluyen en Git; cada persona debe obtenerlos.

## Ejecutar la notebook completa

Instalá las dependencias en el entorno de Python 3.14.5 que prefieras:

```bash
python -m pip install -r requirements.txt
```

Abrí `notebooks/Sistema soporte_prmociones_Instacart.ipynb` con la herramienta de notebooks que uses habitualmente y ejecutá las celdas en orden. Seleccioná el entorno de Python donde instalaste las dependencias.

La base de Optuna incluida ya tiene 28 ensayos completos. Como la notebook requiere al menos 20, reutiliza el mejor ensayo sin iniciar otra búsqueda de hiperparámetros. Sí vuelve a construir las features, entrenar LightGBM y calcular las métricas y explicaciones.
