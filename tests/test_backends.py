import unittest
from mock import Mock
from django.core import mail
from django.conf import settings


settings.configure(
    EMAIL_BACKEND="email_hijacker.backends.hijacker.EmailBackend",
    HIJACKER_EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    HIJACKER_EMAIL_ADDRESS="hijacker@example.org",
)


class TestEmailBackend(unittest.TestCase):

    def test_open(self):
        backend = mail.get_connection(settings.EMAIL_BACKEND)
        backend.hijacked.open = mock = Mock()
        backend.open()
        self.assertTrue(mock.called)
        self.assertEquals(mock.call_count, 1)

    def test_close(self):
        backend = mail.get_connection(settings.EMAIL_BACKEND)
        backend.hijacked.close = mock = Mock()
        backend.close()
        self.assertTrue(mock.called)
        self.assertEquals(mock.call_count, 1)

    def test_email_message(self):
        mail.EmailMessage("Subject", "Message", from_email=None, to=["to@example.org"], cc=["cc@example.org"], bcc=["bcc@example.org"]).send()
        message = mail.outbox.pop()
        self.assertEqual("HIJACKED: Subject", message.subject)
        self.assertEqual((settings.HIJACKER_EMAIL_ADDRESS,), message.to)
        self.assertEqual((), message.cc)
        self.assertEqual((), message.bcc)
