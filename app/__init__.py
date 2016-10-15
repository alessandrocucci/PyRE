# Import di flask e degli operatori di templating
from flask import Flask, render_template
from flask_mail import Mail


# Definizione oggetto WSGI
app = Flask(__name__)
mail = Mail(app)

# Configurazioni
app.config.from_object('config')


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.main.controller import main
# Register blueprint(s)
app.register_blueprint(main)
