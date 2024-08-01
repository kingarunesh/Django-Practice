from django.urls import path

from crud.views import home


urlpatterns = [
    path("", view=home, name="home")
]
