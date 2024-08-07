from django.urls import path

from persite.views import index


urlpatterns = [
    path("", view=index, name="index")
]
