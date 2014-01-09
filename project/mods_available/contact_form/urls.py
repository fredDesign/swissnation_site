# -*- coding: utf-8 -*-

urlpatterns = patterns('',
    url(r'^contact/', include('apps.contact_form.urls')),
    ) + urlpatterns
