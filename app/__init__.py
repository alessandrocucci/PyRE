# Import di flask e degli operatori di templating
from flask import Flask, render_template

# Definizione oggetto WSGI
app = Flask(__name__)

# Configurazioni
app.config.from_object('config')

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
