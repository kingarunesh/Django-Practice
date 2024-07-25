from django.urls import path

from home.views import index, about


urlpatterns = [
    path("", view=index),
    path("about/", view=about)
]