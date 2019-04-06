from django.contrib import admin

from .models import Bb

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_link = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)
