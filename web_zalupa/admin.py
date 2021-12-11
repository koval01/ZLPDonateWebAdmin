from django.contrib import admin

from .models import ServiceDonate, ServiceDonateStatus, SystemSettings

admin.site.register(ServiceDonate)
admin.site.register(ServiceDonateStatus)
admin.site.register(SystemSettings)
admin.site.site_header = 'ЗаЛуПа'
