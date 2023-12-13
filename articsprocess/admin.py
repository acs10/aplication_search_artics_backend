from django.contrib import admin
from .models import UserProfile, SearchHistory

class TextAdmin(admin.ModelAdmin):
    fields = ('body')
    list_display = ['body']


admin.site.register(UserProfile)
admin.site.register(SearchHistory)
