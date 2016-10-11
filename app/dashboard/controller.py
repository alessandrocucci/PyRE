from flask import render_template, Blueprint

dashboard = Blueprint('main', __name__)

@dashboard.route('/dashboard')
def index():
    return render_template('dashboard/index.html')
