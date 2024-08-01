from django.contrib import admin

from crud.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "password"]
    list_display_links = ["id", "name", "email", "password"]