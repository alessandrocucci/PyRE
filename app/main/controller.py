from flask import render_template, Blueprint, redirect, request, url_for, flash
from forms import LoginForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    login_form = LoginForm()
    return render_template('main/index.html', form=login_form)


@main.route('/callforpapers', methods=['GET', 'POST'])
def callforpapers():
    login_form = LoginForm()
    return render_template('main/callforpapers.html', form=login_form)
