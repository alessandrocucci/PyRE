from wtforms import Form, PasswordField, validators, StringField, SelectField
from wtforms.fields.html5 import EmailField


class CallForPapers(Form):
    nome = StringField('nome')
    cognome = StringField('cognome')
    email = StringField('email', [validators.DataRequired(), validators.Email("Inserisci una mail valida")])
    type_of_talk = SelectField(
        'Tipologia',
        choices=[('talk', 'Talk'), ('tutorial', 'Tutorial'), ('workshop', 'Workshop')]
    )
    durata = StringField("Durata Prevista")
