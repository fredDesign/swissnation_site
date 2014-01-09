# -*- coding: utf-8 -*-
"""
Views for contact_form
"""
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import ContactForm

def contact_form(request):
    """View for handling the contact form"""

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_form_sent')
    else:
        form = ContactForm()
    return render_to_response('contact_form/contact_form.html',
                              {'form': form},
                              context_instance=RequestContext(request))
