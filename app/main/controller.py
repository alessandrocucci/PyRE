from flask import render_template, Blueprint, redirect, request, url_for, flash

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/callforpapers', methods=['GET', 'POST'])
def callforpapers():
    return render_template('main/callforpapers.html')


@main.route('/contatti', methods=['GET', 'POST'])
def contatti():
    return render_template('main/contatti.html')
