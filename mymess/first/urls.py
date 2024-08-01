from django.urls import path

from first.views import first_view


urlpatterns = [
    path("first/", view=first_view)
]
