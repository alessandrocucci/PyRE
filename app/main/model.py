from flask_mail import Message
from app import mail


class PyREMail(object):
    def __init__(self, recipients=(), text="", _from=""):
        self.message = Message()
        self.text = text
        self.message.recipients = recipients or ['info@pyre.it']
        self._from = _from
        self.message.sender = 'info@pyre.it'

    def send_mail(self):
        mail.send(self.message)


class ContactMail(PyREMail):
    def __init__(self, *args, **kwargs):
        super(ContactMail, self).__init__(*args, **kwargs)
        self.message.subject = "Messaggio dal Form dei Contatti da {0}".format(self._from)
        self.message.body = self.text


class CallforPapersMail(PyREMail):
    def __init__(self, *args, **kwargs):
        super(CallforPapersMail, self).__init__(*args, **kwargs)
        self.message.subject = "NEW Call of Papers da {0}".format(self._from)
        self.message.body = self.text
