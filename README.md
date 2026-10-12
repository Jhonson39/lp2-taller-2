# Taller 2 - Tienda Virtual con Flask, SQLite y SQLAlchemy

## Descripción del proyecto

Este proyecto consiste en mejorar la tienda virtual del Taller 1, utilizando Flask, SQLite y SQLAlchemy para administrar los productos y sus categorías.

A diferencia del primer taller, donde los productos se cargaban directamente desde un archivo JSON, en este proyecto se utiliza una base de datos SQLite para almacenar la información.

El archivo JSON se conserva para cargar los productos iniciales a la base de datos.

## Objetivo

Desarrollar una aplicación web que permita visualizar productos, consultar sus detalles y filtrar el catálogo por categorías, utilizando una base de datos relacional.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Flask:** framework para desarrollar la aplicación web.
- **Flask-SQLAlchemy:** extensión para conectar Flask con SQLAlchemy.
- **SQLite:** sistema de base de datos.
- **SQLAlchemy:** herramienta para trabajar con la base de datos mediante modelos de Python.
- **HTML:** estructura de las páginas.
- **CSS:** diseño y estilos de la tienda.
- **Jinja2:** creación de plantillas dinámicas.
- **JSON:** archivo utilizado para cargar los productos iniciales.

## Estructura del proyecto

```text
taller2/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── commands.py
│   ├── routes.py
│   ├── data/
│   │   └── productos.json
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── detalle.html
│       └── categorias.html
├── instance/
│   └── tienda.db
├── docs/
│   └── GUIA.md
├── config.py
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

## Funcionalidades

- Mostrar el catálogo de productos.
- Consultar los detalles de cada producto.
- Filtrar los productos por categoría.
- Mostrar las categorías disponibles.
- Indicar si un producto está disponible o agotado.
- Almacenar productos y categorías en SQLite.
- Relacionar cada producto con una categoría.
- Cargar los productos iniciales desde un archivo JSON.
- Evitar insertar productos duplicados utilizando su SKU.
- Mostrar un error 404 cuando un producto no existe.

## Modelos de la base de datos

### Categoría

Representa las categorías de la tienda.

- `id`: identificador de la categoría.
- `nombre`: nombre de la categoría.

### Producto

Representa los productos disponibles en la tienda.

- `id`: identificador del producto.
- `sku`: código único del producto.
- `marca`: marca del producto.
- `nombre`: nombre del producto.
- `precio`: precio del producto.
- `foto`: ruta de la imagen.
- `stock`: cantidad disponible.
- `activo`: indica si el producto está activo.
- `categoria_id`: identificador de la categoría a la que pertenece.

La relación entre las tablas permite que una categoría tenga varios productos y que cada producto pertenezca a una categoría.

## Instalación y ejecución

### 1. Crear el entorno virtual

```bash
python3 -m venv venv
```

### 2. Activar el entorno virtual

En Ubuntu o WSL2:

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar Flask

```bash
export FLASK_APP=run.py
```

### 5. Crear las tablas de la base de datos

```bash
flask init-db
```

### 6. Cargar los productos iniciales

```bash
flask seed-db
```

### 7. Ejecutar la aplicación

```bash
python3 run.py
```

### 8. Abrir la tienda

Ingresar desde el navegador a:

http://127.0.0.1:5000

## Comandos disponibles

| Comando | Descripción |
|---|---|
| `flask init-db` | Crea las tablas de la base de datos. |
| `flask seed-db` | Carga los productos y sus categorías desde el archivo JSON. |
| `flask reset-db` | Elimina las tablas y las vuelve a crear. |

**Importante:** el comando `flask reset-db` elimina los datos almacenados en las tablas. Utilízalo solamente cuando quieras reiniciar la base de datos.

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Muestra el catálogo de productos. |
| `/?categoria=1` | Filtra los productos por el identificador de una categoría. |
| `/producto/<sku>` | Muestra los detalles de un producto específico. |
| `/categorias` | Muestra las categorías disponibles. |

## Base de datos

La base de datos utilizada es SQLite y se encuentra en:

`instance/tienda.db`

Esta base de datos almacena los productos y las categorías, permitiendo consultar la información sin tener que leer el archivo JSON en cada petición.

## Conclusión

Con este taller se amplían los conocimientos adquiridos en el Taller 1, integrando una base de datos SQLite y utilizando SQLAlchemy para administrar la información.

También se aprende a crear modelos, establecer relaciones entre tablas, realizar consultas, filtrar productos y utilizar comandos personalizados de Flask para inicializar y cargar los datos.

