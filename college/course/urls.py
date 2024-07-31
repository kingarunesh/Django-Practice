from django.urls import path

from course.views import course, success_submit


urlpatterns = [
    path("course/", view=course, name="course_page"),
    path("success/", view=success_submit, name="success_submit"),
]
