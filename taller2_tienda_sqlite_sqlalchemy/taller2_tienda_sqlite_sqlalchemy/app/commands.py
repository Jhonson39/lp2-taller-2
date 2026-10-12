import json
from pathlib import Path
import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models import Categoria, Producto

RUTA_JSON = Path(__file__).parent / "data" / "productos.json"

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Crear las tablas de la base de datos."""
    db.create_all()
    click.echo("Tablas creadas correctamente.")

@click.command("reset-db")
@with_appcontext
def reset_db_command():
    """Borrar y volver a crear todas las tablas. ¡Elimina los datos!"""
    db.drop_all()
    db.create_all()
    click.echo("Base de datos reiniciada.")

@click.command("seed-db")
@with_appcontext
def seed_db_command():
    """Cargar productos desde productos.json sin duplicar SKU."""
    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        productos_json = json.load(archivo)

    agregados = 0
    try:
        for datos in productos_json:
            producto_existente = Producto.query.filter_by(sku=datos["sku"]).first()
            if producto_existente:
                continue

            nombre_categoria = datos["categoria"]
            categoria = Categoria.query.filter_by(nombre=nombre_categoria).first()
            if categoria is None:
                categoria = Categoria(nombre=nombre_categoria)
                db.session.add(categoria)
                db.session.flush()

            producto = Producto(
                sku=datos["sku"],
                marca=datos["marca"],
                nombre=datos["nombre"],
                precio=datos["precio"],
                foto=datos.get("foto"),
                stock=datos.get("stock", 0),
                activo=datos.get("activo", True),
                categoria_id=categoria.id
            )
            db.session.add(producto)
            agregados += 1

        db.session.commit()
        click.echo(f"Carga terminada. Productos nuevos agregados: {agregados}.")
    except Exception as error:
        db.session.rollback()
        raise click.ClickException(f"No se pudieron cargar los productos: {error}")
