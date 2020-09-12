from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Customer)
class CustomerImportExportAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "no_motor",
        "phone",
        "email", 
        "date_created",
        "date_h7", 
        "date_h3", 
        "date_phone", 
        "status_h7", 
        "status_h3", 
        "status_telpon",
        "status_whatsapp", 
        "status_kedatangan", 
        "status_call", 
        "tipe_motor", 
        "km_akhir", 
        "ket", 
    )


# admin.site.register(Customer)
admin.site.register(Token)


