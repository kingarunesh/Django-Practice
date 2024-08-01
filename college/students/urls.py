from django.urls import path

from students.views import students

urlpatterns = [
    path("students/<int:id>/<int:my_id>/", view=students, kwargs={"testing": "hello"}, name="students")
]
