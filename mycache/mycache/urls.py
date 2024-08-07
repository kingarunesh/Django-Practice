from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", include("persite.urls")),
    path("", include("perview.urls")),
    path("", include("tfcache.urls")),
    path("", include("lowlevelcache.urls")),
]
