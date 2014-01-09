# -*- coding: utf-8 -*-
"""
Models for contact_form
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from emencia.django.countries.models import Country


class Contact(models.Model):
    """Models for storing contact message"""

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)

    company = models.CharField(_('company / Institution'), max_length=255)
    email = models.EmailField(_('e-mail'))
    phone = models.CharField(_('phone'), max_length=40, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    state = models.CharField(_('state/province'), max_length=255, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('country'),
                                blank=True, null=True)

    message = models.TextField(_('message'))

    optin_newsletter = models.BooleanField(_("do you wish to receive the newsletter?"))

    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)

    def __unicode__(self):
        return 'Contact from %s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
