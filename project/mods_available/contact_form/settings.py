# -*- coding: utf-8 -*-

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'captcha',
    'emencia.django.countries',
    'apps.contact_form')

CONTACT_FORM_TO = []
