=====================
Django Email Hijacker
=====================

.. image:: https://travis-ci.org/jthi3rry/django-email-hijacker.svg?branch=master
    :target: https://travis-ci.org/jthi3rry/django-email-hijacker

.. image:: https://coveralls.io/repos/jthi3rry/django-email-hijacker/badge.png?branch=master
    :target: https://coveralls.io/r/jthi3rry/django-email-hijacker

Django Email Hijacker lets you send emails via your favourite email backend but sends them to a specified email address instead of the intended recipients.

It allows you to send emails via a real backend from a development or staging environment without worrying that an actual user might get sent unintended emails.


Installation
------------
::

    pip install django-email-hijacker


In your development or staging ``settings.py``::


    EMAIL_BACKEND = "email_hijacker.backends.hijacker.EmailBackend"

    HIJACKER_EMAIL_ADDRESS = "hijacker@example.org"
    HIJACKER_EMAIL_BACKEND = "your.real.EmailBackend"


.. note:: Django Email Hijacker uses `Django Pods <https://github.com/OohlaLabs/django-pods>`_.

    It allows for prefix style settings::


        HIJACKER_EMAIL_ADDRESS = "hijacker@example.org"
        HIJACKER_EMAIL_BACKEND = "your.real.EmailBackend"


    Or dictionary style settings::

        HIJACKER = {
            "EMAIL_ADDRESS": "hijacker@example.org",
            "EMAIL_BACKEND": "your.real.EmailBackend"
        }


Running Tests
-------------
::

    tox


Contributions
-------------

All contributions and comments are welcome.

Change Log
----------

v0.3.2
~~~~~~
* Fix #2: exclude tests package

v0.3.1
~~~~~~
* Switch to Semantic Versioning
* Fix issue with parse_requirements for newer versions of pip (>=6.0.0)

v0.3
~~~~
* Use Django Pods for settings

v0.2
~~~~
* Unit tests now use Django 1.7 final instead of RC1

v0.1
~~~~
* Initial
