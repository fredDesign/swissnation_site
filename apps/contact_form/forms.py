# -*- coding: utf-8 -*-
"""
Forms for contact_form
"""
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.forms import ModelForm
from django.template.loader import render_to_string

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, Row, Column, ButtonHolder, Submit

from captcha.fields import ReCaptchaField

from .models import Contact

class ContactForm(ModelForm):
    """Contact Form"""
    error_css_class = 'error'
    required_css_class = 'required'
    
    # Captcha field to use a responsive template
    captcha = ReCaptchaField(attrs={
        'theme': 'custom',
        'custom_theme_widget': 'recaptcha_widget',
    })
   
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))

        super(ContactForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """Save and send"""
        contact = super(ContactForm, self).save()

        context = {'contact': contact,
                   'site': Site.objects.get_current()}

        subject = ''.join(render_to_string(
            'contact_form/contact_form_subject.txt', context).splitlines())
        content = render_to_string('contact_form/contact_form.txt', context)

        send_mail(subject, content,
                  settings.DEFAULT_FROM_EMAIL,
                  settings.CONTACT_FORM_TO,
                  fail_silently=not settings.DEBUG)

        return contact

    class Meta:
        model = Contact
