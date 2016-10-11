from wtforms import Form, StringField, PasswordField, validators, SubmitField


class LoginForm(Form):
    email = StringField('email', [validators.Email()])
    password = PasswordField('password', [validators.DataRequired()])
    submit = SubmitField("Accedi")