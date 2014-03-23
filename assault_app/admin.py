#!/usr/bir/env python

from django.contrib import admin
from assault_app.models import Schools#, SchoolStoryFeed

class SchoolsAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Schools, SchoolsAdmin)

#class SchoolStoryFeedAdmin(admin.ModelAdmin):
#    search_fields = ('title',)

#admin.site.register(SchoolStoryFeed, SchoolStoryFeedAdmin)

