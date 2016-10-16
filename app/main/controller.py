from flask import render_template, Blueprint, request
import json

from forms import ContactForm, CallForPapers, handle_captcha_requests
from model import ContactMail, CallforPapersMail
from config import CAPTCHA_KEY, MAPS_API_KEY

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/callforpapers', methods=['GET'])
def callforpapers():
    form = CallForPapers()
    return render_template('main/callforpapers.html', form=form, key=CAPTCHA_KEY)


@main.route('/send_call_mail', methods=['POST'])
def send_call_mail():
    form = CallForPapers()
    if form.errors:
        return json.dumps({'status': 'KO', 'message': form.errors})
    elif form.validate_on_submit() and handle_captcha_requests(request.form['g-recaptcha-response']):
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
        try:
            mail.send_mail()
        except Exception:
            return json.dumps({'status': 'KO', 'message': "ERRORE: impossibile inviare la mail"})
        else:
            return json.dumps({'status': 'OK', 'message': "Messaggio inviato correttamente"})
    return json.dumps({})


@main.route('/contatti', methods=['GET'])
def contatti():
    form = ContactForm()
    return render_template('main/contatti.html', form=form, key=CAPTCHA_KEY, maps_key=MAPS_API_KEY)


@main.route('/send_contact_mail', methods=['POST'])
def send_contact_mail():
    form = ContactForm()
    validated = form.validate_on_submit()
    if form.errors:
        return json.dumps({'status': 'KO', 'message': form.errors})
    elif validated and handle_captcha_requests(request.form['g-recaptcha-response']):
        mail = ContactMail(text=form.messaggio.data.encode('utf-8'), _from=" ".join((form.nome.data, form.cognome.data, form.email.data)))
        try:
            mail.send_mail()
        except Exception:
            return json.dumps({'status': 'KO', 'message': "ERRORE: impossibile inviare la mail"})
        else:
            return json.dumps({'status': 'OK', 'message': "Messaggio inviato correttamente"})
    return json.dumps({})


