# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail.backends.base import BaseEmailBackend

try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading import import_by_path as import_string  # NOQA

from ..apps import EmailHijacker


class EmailBackend(BaseEmailBackend):

    def __init__(self, *args, **kwargs):
        super(EmailBackend, self).__init__(*args, **kwargs)
        self.hijacked = import_string(EmailHijacker.EMAIL_BACKEND)(*args, **kwargs)

    def open(self):
        self.hijacked.open()

    def close(self):
        self.hijacked.close()

    def send_messages(self, email_messages):
        for email in email_messages:
            email.to = (EmailHijacker.EMAIL_ADDRESS,)
            email.bcc = ()
            email.cc = ()
            email.subject = 'HIJACKED: {}'.format(email.subject)
        self.hijacked.send_messages(email_messages)
