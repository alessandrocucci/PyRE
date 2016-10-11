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
            flash("That's good")
        else:
            flash("Not Good")
    return redirect(url_for('main.index'))
