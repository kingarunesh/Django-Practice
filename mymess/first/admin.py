from django.contrib import admin

from first.models import Aohan



@admin.register(Aohan)
class AohanAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password"]
    list_display_links = ["id", "name", "email", "password"]