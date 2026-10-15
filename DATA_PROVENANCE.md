# Procedencia de los datos

Dataset: *The Instacart Online Grocery Shopping Dataset 2017*. Fuente oficial: https://www.instacart.com/datasets/grocery-shopping-2017 . Anuncio y cita solicitada: https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2 . Términos: https://gist.github.com/jeremystan/582eba13d6ee27ed465c43dc78934700 .

Instacart permite uso no comercial y prohíbe proporcionar o poner el dataset a disposición de terceros. Por eso los CSV originales están dentro de esta carpeta **local** para reproducir el trabajo, pero `.gitignore` impide publicarlos con Git. La base DuckDB, que contiene copias de las tablas, también se ignora. Git LFS no cambia esta condición.

Al clonar el repositorio, cada persona debe obtener el dataset desde la fuente oficial y aceptar sus términos. Colocar estos seis archivos en `data/raw/`:

- `orders.csv`
- `order_products__prior.csv`
- `order_products__train.csv`
- `products.csv`
- `departments.csv`
- `aisles.csv`

La copia local se verificó con `manifest.sha256`. Tras adquirir los archivos, ejecutar `python scripts/verify_package.py` para comprobar que coinciden byte a byte. Si la fuente entrega una versión distinta, la verificación fallará y los resultados podrían variar. El notebook puede reconstruir `data/processed/instacart.duckdb` desde esos CSV; no hace falta compartir esa base.
