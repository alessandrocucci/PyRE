from wtforms import validators, StringField, SelectField, TextAreaField
from flask_wtf import FlaskForm
import requests
from config import CAPTCHA_KEY_SECRET, CSRF_SESSION_KEY


def handle_captcha_requests(response_from_form):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data_dict = {
        'secret': CAPTCHA_KEY_SECRET,
        'response': response_from_form
    }
    res = requests.post(url, data=data_dict).json()
    return res['success']


class DataRequired(validators.DataRequired):
    def __init__(self):
        super(DataRequired, self).__init__(message="Questo campo e' obbligatorio")


class CallForPapers(FlaskForm):
    SECRET_KEY = CSRF_SESSION_KEY
    nome = StringField(
        'nome',
        [DataRequired()],
        render_kw={
            "placeholder": "Nome",
            "class_": "form-control input-lg"
        })
    cognome = StringField(
        'cognome',
        [DataRequired()],
        render_kw={
            "placeholder": "Cognome",
            "class_": "form-control input-lg"
        })
    email = StringField(
        'email',
        [DataRequired(), validators.Email("Inserisci una mail valida")],
        render_kw={
            "placeholder": "Email",
            "class_": "form-control input-lg"
        })
    argomento = StringField(
        'argomento',
        [DataRequired()],
        render_kw={
            "placeholder": "Titolo",
            "class_": "form-control input-lg"
        })
    abstract = TextAreaField(
        'abstract',
        [DataRequired()],
        render_kw={
            "placeholder": "Riassunto",
            "class_": "form-control input-lg",
            "rows": 5
        })
    type_of_talk = SelectField(
        'Tipologia',
        choices=[('', '-- Tipo Intervento --'), ('talk', 'Talk'), ('tutorial', 'Tutorial'), ('workshop', 'Workshop')],
        render_kw={
            "class_": "form-control input-lg"
        }
    )
    durata = StringField(
        "Durata Prevista",
        render_kw={
            "placeholder": "Durata",
            "class_": "form-control input-lg",
            "rows": 5
        }
    )


class ContactForm(FlaskForm):
    """
    Classe form per invio mail dalla pagina dei contatti.

    Il submit e il reCAPTCHA li inserisco secchi nel template.
    """
    SECRET_KEY = CSRF_SESSION_KEY
    nome = StringField(
        'nome',
        [DataRequired()],
        render_kw={
            "placeholder": "Nome",
            "class_": "form-control input-lg"
        })
    cognome = StringField(
        'cognome',
        [DataRequired()],
        render_kw={
            "placeholder": "Cognome",
            "class_": "form-control input-lg"
        })
    email = StringField(
        'email',
        [DataRequired(), validators.Email("Inserisci una mail valida")],
        render_kw={
            "placeholder": "Email",
            "class_": "form-control input-lg"
        })
    messaggio = TextAreaField(
        'messaggio',
        [DataRequired()],
        render_kw={
            "placeholder": "Messaggio",
            "class_": "form-control input-lg",
            "rows": 5
        })
