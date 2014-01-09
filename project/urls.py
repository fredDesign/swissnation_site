# -*- coding: utf-8 -*-

# Import from the Standard Library
import os

# Import from django
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)
urlpatterns += staticfiles_urlpatterns()

urlpatterns = i18n_patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')), # Cause troubles with docutils usage like with codemirror
    url(r'^admin/', include(admin.site.urls)),
)

# Mods system
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
mods = os.path.join(PROJECT_PATH, 'mods_enabled')
mods = [ os.path.join(mods, x) for x in os.listdir(mods) ]
mods.sort()
for mod in mods:
    mod = os.path.join(mod, 'urls.py')
    if os.path.isfile(mod):
        execfile(mod)

# Debug
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
