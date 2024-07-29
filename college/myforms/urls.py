from django.urls import path

from myforms.views import my_forms


urlpatterns = [
    path("my-forms/", view=my_forms, name="my_forms")
]
