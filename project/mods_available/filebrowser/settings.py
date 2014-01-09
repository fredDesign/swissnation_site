# -*- coding: utf-8 -*-
import os

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'filebrowser',
                              before="djangocms_text_ckeditor")

# Needed for compatibility with filebrowser_no_grapelli that use
# ADMIN_MEDIA_PREFIX when tinymce is not installed, sadly this raise a
# warning by Django >= 1.5
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, "admin/")
