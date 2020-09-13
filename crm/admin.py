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
        "message1",
        "message2",
        "message3",
        "message4",
        "status_message1",
        "status_message2",
        "status_message3",
        "status_message4",     
    )


class SendWAAdmin(admin.ModelAdmin):

    list_display = (
        "messages",
        "message", 
        # "image",
        "media_url", 
        "type_media_url", 
        "location",
        "device",
    )

    fields = (
        "messages",
        "message",   
        # "image",
        "media_url", 
        "type_media_url", 
        "location",
        "device",
    )

class DeviceAdmin(admin.ModelAdmin):

    list_display = (
        "phone",
        "device_code", 
        "token_api", 
        "server_address", 
        "location",
    )

    fields = (
        "phone",
        "device_code", 
        "token_api", 
        "server_address", 
        "location",
    )


admin.site.register(Device, DeviceAdmin)
admin.site.register(SendWA, SendWAAdmin)
admin.site.register(Token)


