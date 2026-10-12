import os

# La ruta de la base de datos es absoluta para evitar problemas al ejecutar Flask.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "tienda.db")

class Config:
    SECRET_KEY = "clave-de-practica-cambiar-en-produccion"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
