from django.contrib import admin

from course.models import Course


#!      simple way to connect with admin
# admin.site.register(Course)



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "course_id", "title", "price", "email"]
    list_display_links = ["id", "course_id", "title", "price", "email"]

# admin.site.register(Course, admin_class=CourseAdmin)