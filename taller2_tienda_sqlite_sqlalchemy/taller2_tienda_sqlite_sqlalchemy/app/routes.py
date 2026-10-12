from flask import Blueprint, render_template, request
from app.models import Categoria, Producto

main = Blueprint("main", __name__)

@main.route("/")
def index():
    categoria_id = request.args.get("categoria", type=int)
    consulta = Producto.query.filter_by(activo=True)

    if categoria_id:
        consulta = consulta.filter_by(categoria_id=categoria_id)

    productos = consulta.order_by(Producto.nombre).all()
    categorias = Categoria.query.order_by(Categoria.nombre).all()
    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_seleccionada=categoria_id
    )

@main.route("/producto/<sku>")
def detalle(sku):
    producto = Producto.query.filter_by(sku=sku).first_or_404()
    return render_template("detalle.html", producto=producto)

@main.route("/categorias")
def categorias():
    categorias = Categoria.query.order_by(Categoria.nombre).all()
    return render_template("categorias.html", categorias=categorias)
