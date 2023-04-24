from django.contrib import admin
from . import models

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'saldo')

admin.site.register(models.Cliente, ClienteAdmin)