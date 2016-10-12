from wtforms import Form, PasswordField, validators
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    email = EmailField('email', [validators.DataRequired(), validators.Email("Inserisci una mail valida")])
    password = PasswordField('password', [validators.DataRequired()])