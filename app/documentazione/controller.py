from flask import render_template, Blueprint

docs = Blueprint('docs', __name__)

@docs.route('/docs')
def documentazione():
    return render_template('documentazione/index.html')
