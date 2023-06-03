from django.contrib import admin

from .models import Tag, Story, Chapter

# Register your models here.

admin.site.register(Tag)
admin.site.register(Story)
admin.site.register(Chapter)