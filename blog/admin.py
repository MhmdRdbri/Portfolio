from django.contrib import admin
from .models import *


class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Article",
            {
                "fields": ["author", "title", "slug", "body", "image", "alt", "pub_date"],
            },
        ),
        (
            "Seo",
            {
                "classes": ["collapse"],
                "fields": ["pagetitle", "description", "canonical", "localeOg", "typeOg", "titleOg", "descriptionOg",
                           "site_name", "widthOg", "heightOg"],
            },
        ),
    ]


admin.site.register(Article, FlatPageAdmin)
admin.site.register(Message)
admin.site.register(Tags)
