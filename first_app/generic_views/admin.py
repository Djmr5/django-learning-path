from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Cat)
admin.site.register(models.Horse)