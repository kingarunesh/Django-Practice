from django.urls import path

from about.views import my_about


urlpatterns = [
    path("my-about/", view=my_about)
]