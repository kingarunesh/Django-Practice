from django.urls import path

from lowlevelcache.views import low_level_cache, delete_cache


urlpatterns = [
    path("low-level-cache/", view=low_level_cache),
    path("clear/", view=delete_cache)
]
