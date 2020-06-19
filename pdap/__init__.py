from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_classes as config_env


def create_app(config_class='development'):
    app = Flask(__name__)
    app.config.from_object(config_env[config_class])

    from pdap.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
        import pdap.views
    

    return app