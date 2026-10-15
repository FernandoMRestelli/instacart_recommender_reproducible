# Recomendador Instacart — paquete reproducible

Esta carpeta contiene la notebook auditada, dependencias fijadas, estado de Optuna y, **sólo localmente**, los seis CSV originales, la base DuckDB y un checkpoint de LightGBM de una corrida separada. El repositorio Git puede publicarse sin los datos gracias a `.gitignore`; consultá [DATA_PROVENANCE.md](DATA_PROVENANCE.md) antes de subirlo. No equivale a una reejecución completa verificada de la notebook.

## Estructura

- `notebooks/01_Tesis_Marketing_Instacart_auditada.ipynb`: pipeline principal con rutas relativas; ejecutar celdas en orden.
- `data/raw/`: seis CSV originales, sólo local y fuera de Git.
- `data/processed/`: caché DuckDB, se reconstruye desde los CSV.
- `optuna/`: estudio SQLite con trials y parámetros; se conserva en Git.
- `models/`: checkpoint local y modelo generado al ejecutar la notebook; fuera de Git por defecto.
- `outputs/`: exportaciones, gráficos y tablas regenerables; fuera de Git.
- `manifest.sha256`: hashes de los archivos locales esenciales.
- `scripts/verify_package.py`: comprueba estructura, hashes y que Git omite datos/modelos.

## Reproducción

Recomendado: macOS y Python 3.14.5, la plataforma y versión usadas al preparar esta copia. `requirements.txt` contiene dependencias directas fijadas. `requirements-lock-macos.txt` registra el entorno completo de referencia, pero puede no ser portable a otros sistemas.

```bash
cd instacart-recommender-reproducible
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock-macos.txt
python scripts/verify_package.py  # Para exigir además todos los artefactos locales: --strict
python -m ipykernel install --user --name instacart-repro --display-name "Instacart reproducible"
python -m pip install jupyterlab
python -m jupyterlab
```

`jupyterlab` es una interfaz opcional; no forma parte del entorno de cómputo usado para los resultados. Para instalar sólo las dependencias de ejecución, usar `requirements-lock-macos.txt` y abrir la notebook desde una interfaz Jupyter ya disponible. En otro sistema operativo, usar `requirements.txt` (versiones directas fijadas). Elegir el kernel `Instacart reproducible`. Abrir Jupyter desde la raíz de esta carpeta (o `notebooks/`) y ejecutar `notebooks/01_Tesis_Marketing_Instacart_auditada.ipynb` de arriba abajo. Si el repositorio viene de GitHub, adquirir los CSV de la fuente oficial y colocarlos en `data/raw/` antes de verificar o ejecutar. La notebook construye DuckDB si falta.

El estudio Optuna tiene trials previos. Para **reproducir la selección conservada**, dejar `optuna/optuna_study_temporal_NDCG10_v3.db`; la notebook carga el estudio y usa el mejor trial disponible. Para una búsqueda nueva desde cero, trabajar en otra copia de la carpeta y quitar allí la base de Optuna, aceptando el tiempo de entrenamiento y la posible variación por paralelismo/hardware. No sobrescribir el estudio archivado. La semilla del pipeline es 42.

La notebook guarda el nuevo modelo seleccionado en `models/lightgbm_model_auditado.txt`, y las tablas y figuras en `outputs/`. El checkpoint ya presente en `models/` corresponde a otra corrida y está documentado en `models/README.md`.

## Alcance de reproducibilidad

Las versiones, semillas, CSV y estado de Optuna están registrados. La equivalencia numérica exacta en otra máquina no está garantizada por operaciones paralelas, compilación de LightGBM o diferencias de plataforma. Esta carpeta fue validada estructuralmente y contra los datos/artefactos existentes; **no se volvió a entrenar ni a ejecutar toda la notebook** durante el empaquetado. La notebook requiere memoria suficiente para su pipeline completo.

## Publicación

```bash
git status --short --untracked-files=all
git check-ignore data/raw/orders.csv data/processed/instacart.duckdb models/lightgbm_reentrenado_usuario1_20261015.txt
git add .
git status --short
```

Revisar `git status --short` antes de crear el commit y subir a GitHub. Los CSV, la base DuckDB, el checkpoint local, y las salidas deben permanecer fuera del commit. Si se desea compartir cualquier modelo o salida derivados del dataset, revisar primero sus derechos y contenido. El estudio Optuna de 164 KB contiene hiperparámetros y métricas de los trials, no los CSV originales.
