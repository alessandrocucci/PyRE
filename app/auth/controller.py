from flask import render_template, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/auth')
def index():
    return render_template('auth/index.html')
