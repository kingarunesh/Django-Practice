from django.urls import path

from first.views import register


urlpatterns = [
    path("register/", view=register)
]
