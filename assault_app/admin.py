#!/usr/bir/env python

from django.contrib import admin
from assault_app.models import Schools, Comment

class SchoolsAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Schools, SchoolsAdmin)

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)

#class SchoolStoryFeedAdmin(admin.ModelAdmin):
#    search_fields = ('title',)

#admin.site.register(SchoolStoryFeed, SchoolStoryFeedAdmin)

