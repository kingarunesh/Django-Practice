from django.urls import path

from products.views import plugins, themes


urlpatterns = [
    path("plugins/", view=plugins, name="plugins"),
    path("themes/", view=themes, name="themes")
]
