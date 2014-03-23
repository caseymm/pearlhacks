#!/usr/bir/env python

from django.contrib import admin
from assault_app.models import Schools

class SchoolsAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Schools, SchoolsAdmin)

