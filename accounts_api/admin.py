from django.contrib import admin

from . import models

admin.site.register(models.UserAccount)
admin.site.register(models.UserMailList)
