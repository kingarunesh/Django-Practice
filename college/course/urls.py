from django.urls import path

from course.views import course


urlpatterns = [
    path("course/", view=course, name="course_page")
]
