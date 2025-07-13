import os
from flask_admin import Admin
from models import db, User, Planet, Character, Favorite  # Importa todos los modelos
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Añade todos los modelos que quieres administrar
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(Favorite, db.session))
