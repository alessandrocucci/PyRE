# Import di flask e degli operatori di templating
from flask import Flask, render_template

# Import a module / component using its blueprint handler variable (mod_auth)
from app.main.controller import main

# Inizializzo LoginManager
from flask.ext.login import LoginManager

login_manager = LoginManager()

# Definizione oggetto WSGI
app = Flask(__name__)

# Configurazioni
app.config.from_object('config')
login_manager.init_app(app)


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(main)
