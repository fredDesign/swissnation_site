# -*- coding: utf-8 -*-
"""
Models for contact_form
"""
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    'apps.contact_form.views',
    url(r'^$', 'contact_form', name='contact_form'))

view = TemplateView.as_view(template_name='contact_form/contact_form_sent.html')
urlpatterns += patterns(
    'django.views.generic.simple',
    url(r'^sent/$', view, name='contact_form_sent'))
