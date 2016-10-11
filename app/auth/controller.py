from flask import render_template, Blueprint

auth = Blueprint('main', __name__)

@auth.route('/auth')
def index():
    return render_template('auth/index.html')
