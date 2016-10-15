from flask_mail import Message
from app import mail, app


class PyREMail(object):
    def __init__(self, recipients=(), text="", _from="", attachments=()):
        self.message = Message()
        self.message.text = text
        self._from = _from
        self.attachements = attachments
        self.message.sender = 'info@pyre.it'
        if not recipients:
            self.recipients = ['info@pyre.it']

    def send_mail(self):
        if self.attachements:
            for f in self.attachements:
                with app.open_resource(f) as fp:
                    self.message.attach(f, fp.read())
        mail.send(self.message)


class ContactMail(PyREMail):
    def __init__(self, *args, **kwargs):
        super(ContactMail, self).__init__(*args, **kwargs)
        self.message.subject = "Messaggio dal Form dei Contatti da ".format(self._from)


class CallforPapersMail(PyREMail):
    def __init__(self, *args, **kwargs):
        super(CallforPapersMail, self).__init__(*args, **kwargs)
        self.message.subject = "NEW Call of Papers da ".format(self._from)
