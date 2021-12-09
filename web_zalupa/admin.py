from django.contrib import admin

from .models import ServiceDonate, ServiceDonateStatus

admin.site.register(ServiceDonate)
admin.site.register(ServiceDonateStatus)
admin.site.site_header = 'ЗаЛуПа'
