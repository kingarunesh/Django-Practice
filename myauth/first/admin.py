from django.contrib import admin

from first.models import Aohan, Blog


@admin.register(Aohan)
class AohanAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city"]



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]