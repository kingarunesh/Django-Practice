from django.contrib import admin

from course.models import Course, Member


#!      simple way to connect with admin
# admin.site.register(Course)



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "course_id", "title", "price", "email"]
    list_display_links = ["id", "course_id", "title", "price", "email"]

# admin.site.register(Course, admin_class=CourseAdmin)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["teacher_name", "student_name", "contact_number", "email", "joined_date"]
    list_display_links = ["teacher_name", "student_name", "contact_number", "email", "joined_date"]