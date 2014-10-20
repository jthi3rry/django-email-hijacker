try:
    from django.apps import AppConfig
except:  # pragma: no cover
    class AppConfig(object):
        def __init__(self, *args, **kwargs):
            pass

from pods.apps import AppSettings


class EmailHijacker(AppSettings, AppConfig):
    name = "email_hijacker"
    settings_module = "email_hijacker.defaults"
    settings_key = "HIJACKER"
