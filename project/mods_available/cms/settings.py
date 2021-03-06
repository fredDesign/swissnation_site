# -*- coding: utf-8 -*-


MIDDLEWARE_CLASSES += (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS,
    'cms',
    'mptt',
    'menus',
    'sekizai',
    # Plugins
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    #'cms.plugins.snippet',
    'snippet',
    'cms.plugins.teaser',
    #'cms.plugins.text', # disabled to use `djangocms_text_ckeditor` instead, see mod "ckeditor"
    'cms.plugins.video',
    'cms.plugins.twitter',
)

TEMPLATE_CONTEXT_PROCESSORS = add_to_tuple(TEMPLATE_CONTEXT_PROCESSORS,
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

CMS_TEMPLATES = (
    ('cms/1_cols.html', '1 column'),
    ('cms/2_cols.html', '2 columns'),
    ('cms/3_cols.html', '3 columns'),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['de', 'fr'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback':False,
        },
        {
            'code': 'de',
            'name': gettext('Deutsch'),
            'fallbacks': ['en', 'fr'],
            'public': True,
        },
        {
            'code': 'fr',
            'name': gettext('French'),
            'public': True,
        },
    ],
    2: [
        {
            'code': 'nl',
            'name': gettext('Dutch'),
            'public': True,
            'fallbacks': ['en'],
        },
    ],
    'default': {
        'fallbacks': ['en', 'de', 'fr'],
        'redirect_on_fallback':True,
        'public': False,
        'hide_untranslated': False,
    }
}

CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_SOFTROOT = True

# Djangocodemirror settings for cms_snippet plugin
CODEMIRROR_SETTINGS = {
    'cms_snippet': {
        'mode': "xml",
        'lineWrapping': True,
        'lineNumbers': True,
        'search_enabled': True,
        'embed_settings': True,
        'add_jquery': True,
        'lib_buttons_path': 'djangocodemirror/snippet_buttons.js',
    },
}
