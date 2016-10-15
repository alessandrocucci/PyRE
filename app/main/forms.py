from wtforms import Form, validators, StringField, SelectField, TextAreaField
import requests
from config import CAPTCHA_KEY_SECRET


def handle_captcha_requests(response_from_form):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    to_send = {
        'secret': CAPTCHA_KEY_SECRET,
        'response': response_from_form
    }
    res = requests.post(url, json=to_send).json()
    return res['success']


class CallForPapers(Form):
    nome = StringField('nome')
    cognome = StringField('cognome')
    email = StringField('email', [validators.DataRequired(), validators.Email("Inserisci una mail valida")])
    type_of_talk = SelectField(
        'Tipologia',
        choices=[('talk', 'Talk'), ('tutorial', 'Tutorial'), ('workshop', 'Workshop')]
    )
    durata = StringField("Durata Prevista")


class ContactForm(Form):
    """
    Classe form per invio mail dalla pagina dei contatti.

    Il submit e il reCAPTCHA li inserisco secchi nel template.
    """
    nome = StringField(
        'nome',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Nome",
            "class_": "form-control input-lg"
        })
    cognome = StringField(
        'cognome',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Cognome",
            "class_": "form-control input-lg"
        })
    email = StringField(
        'email',
        [validators.DataRequired(), validators.Email("Inserisci una mail valida")],
        render_kw={
            "placeholder": "Email",
            "class_": "form-control input-lg"
        })
    messaggio = TextAreaField(
        'messaggio',
        [validators.DataRequired()],
        render_kw={
            "placeholder": "Messaggio",
            "class_": "form-control input-lg",
            "rows": 5
        })
