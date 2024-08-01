from django.urls import path

from crud.views import home, delete_student


urlpatterns = [
    path("", view=home, name="home"),
    path("delete/<int:id>/", view=delete_student, name="delete_student")
]
