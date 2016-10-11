# Import di flask e degli operatori di templating
from flask import Flask, render_template

# Import a module / component using its blueprint handler variable (mod_auth)
from app.documentazione.controller import docs
from app.main.controller import main
from app.dashboard.controller import dashboard
from app.auth.controller import auth

# Definizione oggetto WSGI
app = Flask(__name__)

# Configurazioni
app.config.from_object('config')

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(docs)
app.register_blueprint(main)
app.register_blueprint(dashboard)
app.register_blueprint(auth)
