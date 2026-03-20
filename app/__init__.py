import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # MODIFICA QUI:
    # os.environ.get('NOME_VAR', 'valore_default')
    # Se trova SECRET_KEY nel sistema/file .env la usa.
    # Altrimenti usa 'dev' (utile per non bloccarci se manca il file).
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DATABASE=os.path.join(app.instance_path, 'video_app.sqlite'),
    )
    

    # --- AGGIUNGI QUESTO ---
    from . import db

    db.init_app(app)
    # -----------------------

    # --- REGISTRAZIONE BLUEPRINTS ---
    from . import main

    app.register_blueprint(main.bp)

    return app
