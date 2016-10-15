from flask import render_template, Blueprint, redirect, request, url_for, flash
from forms import ContactForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/callforpapers', methods=['GET', 'POST'])
def callforpapers():
    return render_template('main/callforpapers.html')


@main.route('/contatti', methods=['GET', 'POST'])
def contatti():
    from config import CAPTCHA_KEY
    form = ContactForm()
    return render_template('main/contatti.html', form=form, key=CAPTCHA_KEY)
