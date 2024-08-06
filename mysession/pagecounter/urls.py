from django.urls import path

from pagecounter.views import page_counter


urlpatterns = [
    path("count/", view=page_counter)
]
