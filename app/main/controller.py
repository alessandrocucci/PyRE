from flask import render_template, Blueprint, request
from werkzeug.utils import secure_filename

from forms import ContactForm, CallForPapers, handle_captcha_requests
from model import ContactMail, CallforPapersMail
from config import CAPTCHA_KEY, MAPS_API_KEY

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/callforpapers', methods=['GET', 'POST'])
def callforpapers():
    form = CallForPapers()
    if request.method == 'POST' and form.validate_on_submit() and handle_captcha_requests(request.form['g-recaptcha-response']):
        messaggio = """
        Nome: {nome}
        Cognome: {cognome}
        Mail: {email}

        Titolo: {titolo}
        Tipologia: {tipo}
        Durata: {durata}
        Abstract:
        {riassunto}
        """.format(
            nome=form.nome.data.encode('utf-8'),
            cognome=form.cognome.data.encode('utf-8'),
            email=form.email.data.encode('utf-8'),
            titolo=form.argomento.data.encode('utf-8'),
            tipo=form.type_of_talk.data.encode('utf-8'),
            durata=form.durata.data.encode('utf-8'),
            riassunto=form.abstract.data.encode('utf-8')
        )
        mail = CallforPapersMail(text=messaggio, _from=" ".join((form.nome.data, form.cognome.data)))
        mail.send_mail()
    return render_template('main/callforpapers.html', form=form, key=CAPTCHA_KEY)


@main.route('/contatti', methods=['GET', 'POST'])
def contatti():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit() and handle_captcha_requests(request.form['g-recaptcha-response']):
        mail = ContactMail(text=form.messaggio.data.encode('utf-8'), _from=" ".join((form.nome.data, form.cognome.data, form.email.data)))
        mail.send_mail()
    return render_template('main/contatti.html', form=form, key=CAPTCHA_KEY, maps_key=MAPS_API_KEY)
