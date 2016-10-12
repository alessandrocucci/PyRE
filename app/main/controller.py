from flask import render_template, Blueprint, redirect, request, url_for, flash
from forms import LoginForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    login_form = LoginForm()
    return render_template('main/index.html', form=login_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # controlla login
            pass
        else:
            # non sei autenticato
            pass
    return redirect(url_for('main.index'))
