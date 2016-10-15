from flask import render_template, Blueprint, request
from werkzeug.utils import secure_filename

from forms import ContactForm, CallForPapers, handle_captcha_requests
from model import ContactMail, CallforPapersMail
from config import CAPTCHA_KEY

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/callforpapers', methods=['GET', 'POST'])
def callforpapers():
    form = CallForPapers()
    if request.method == 'POST' and form.validate() and handle_captcha_requests(request.form['g-recaptcha-response']):
        if request.files['file']:
            f = request.files['file']
            f.save(secure_filename(f.filename))
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
            nome=form.nome.data,
            cognome=form.cognome.data,
            email=form.email.data,
            titolo=form.argomento.data,
            tipo=form.type_of_talk.data,
            durata=form.durata.data,
            riassunto=form.abstract.data
        )
        mail = CallforPapersMail(text=messaggio, _from=" ".join((form.nome.data, form.cognome.data)), attachments=[request.files['file']])
        mail.send_mail()
    return render_template('main/callforpapers.html', form=form, key=CAPTCHA_KEY)


@main.route('/contatti', methods=['GET', 'POST'])
def contatti():
    form = ContactForm()
    if request.method == 'POST' and form.validate() and handle_captcha_requests(request.form['g-recaptcha-response']):
        mail = ContactMail(text=form.messaggio.data, _from=" ".join((form.nome.data, form.cognome.data, form.email.data)))
        mail.send_mail()
    return render_template('main/contatti.html', form=form, key=CAPTCHA_KEY)
