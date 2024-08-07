from django.contrib import admin

from first.models import First


@admin.register(First)
class FirstAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]