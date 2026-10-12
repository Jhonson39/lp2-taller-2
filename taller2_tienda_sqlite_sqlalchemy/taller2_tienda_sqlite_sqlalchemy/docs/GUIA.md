# Taller 2 — Guía para principiantes (VS Code)

## ¿Qué cambia respecto al Taller 1?
Antes, la tienda leía los productos directamente de un archivo JSON. Ahora ese JSON se usa para cargar los datos a una base de datos SQLite. SQLAlchemy ayuda a consultar esa base de datos desde Python.

## 1. Abrir el proyecto
1. Descomprime el ZIP.
2. Abre Visual Studio Code.
3. Selecciona **Archivo > Abrir carpeta** y abre `taller2_tienda_sqlite_sqlalchemy`.
4. Abre **Terminal > Nueva terminal**.

## 2. Preparar el entorno en Ubuntu/WSL2
Ejecuta los comandos uno por uno:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
```

## 3. Crear la base y cargar productos
Ejecuta en este orden:

```bash
flask init-db
flask seed-db
```

El primer comando crea las tablas. El segundo lee `app/data/productos.json` y guarda los productos. Si lo ejecutas de nuevo, no duplica los SKU que ya existen.

## 4. Iniciar la tienda

```bash
python3 run.py
```

Abre `http://127.0.0.1:5000` en el navegador. Para detener el servidor, vuelve a la terminal y presiona `Ctrl+C`.

## 5. Qué probar
- `http://127.0.0.1:5000/` — catálogo.
- `http://127.0.0.1:5000/?categoria=1` — filtro por categoría (el número depende de la base).
- `http://127.0.0.1:5000/producto/TEC-001` — detalle de producto.
- `http://127.0.0.1:5000/producto/NO-EXISTE` — debe mostrar 404.
- `http://127.0.0.1:5000/categorias` — categorías y cantidad de productos.

## 6. Comandos importantes
- `flask init-db`: crea tablas.
- `flask seed-db`: importa los productos desde JSON.
- `flask reset-db`: borra los datos y crea tablas nuevas. **Cuidado: elimina los datos existentes.**

Si abres una terminal nueva, vuelve a activar el entorno (`source venv/bin/activate`) y ejecutar `export FLASK_APP=run.py`.

## Archivos importantes
- `config.py`: configuración de la base de datos.
- `app/extensions.py`: instancia de SQLAlchemy.
- `app/models.py`: tablas Categoria y Producto.
- `app/commands.py`: comandos para crear y poblar la base.
- `app/routes.py`: páginas y consultas.
- `app/data/productos.json`: datos iniciales.
- `instance/tienda.db`: archivo SQLite, se crea al inicializar la base.

Nota: los archivos están preparados siguiendo la guía, pero debes ejecutar los comandos en tu computador para confirmar que funciona en tu instalación.
