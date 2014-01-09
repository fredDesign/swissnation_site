# Import from django
from datetime import datetime
from django.contrib import admin
from django.conf.urls import patterns, url
from django.utils.translation import ugettext as _

# Import from django-excel-response
from excel_response import ExcelResponse

# Import from here
from models import Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'creation_date'
    list_display = ('first_name', 'last_name', 'company',
                    'city', 'country', 'creation_date')

    search_fields = ('first_name', 'last_name', 'company',
                     'email', 'phone', 'city', 'state')
    fieldsets = ((None, {'fields': ('first_name', 'last_name',
                                    'company')}),
                 (None, {'fields': ('message',)}),
                 (_('Contact'), {'fields': ('email', 'phone')}),
                 (_('Address'), {'fields': ('city', 'state', 'country')}),)
    actions_on_top = False
    actions_on_bottom = True

    def export(self, request):
        return ExcelResponse(
            Contact.objects.all(),
            'contact_form_%s' % datetime.now().strftime('%Y%m%d%H%M'))

    def get_urls(self):
        urls = super(ContactAdmin, self).get_urls()
        my_urls = patterns(
            '',
            url(r'^export/$', self.admin_site.admin_view(self.export))
            )
        return my_urls + urls


admin.site.register(Contact, ContactAdmin)
