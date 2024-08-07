from django.urls import path

from tfcache.views import first_view

urlpatterns = [
    path("tf-first/", view=first_view)
]
