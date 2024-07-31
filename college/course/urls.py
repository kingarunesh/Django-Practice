from django.urls import path

from course.views import course, success_submit, course_delete


urlpatterns = [
    path("course/", view=course, name="course_page"),
    path("success/", view=success_submit, name="success_submit"),
    path("delete-course/<int:id>/", view=course_delete, name="course_delete"),
]
