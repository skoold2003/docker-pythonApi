from flask import Flask
from pdap.models import db

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db.init_app(app)
with app.app_context():
    db.create_all()

import pdap.views

