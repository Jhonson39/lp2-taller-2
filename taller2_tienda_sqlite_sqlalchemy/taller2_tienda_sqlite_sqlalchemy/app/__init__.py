import os
from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Crear la carpeta instance si todavía no existe.
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    # Importar modelos para que SQLAlchemy conozca las tablas.
    from app import models
    from app.commands import init_db_command, reset_db_command, seed_db_command
    app.cli.add_command(init_db_command)
    app.cli.add_command(reset_db_command)
    app.cli.add_command(seed_db_command)

    from app.routes import main
    app.register_blueprint(main)

    return app
