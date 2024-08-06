from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", include("mycookies.urls")),
    path("", include("mysessions.urls")),
    path("", include("pagecounter.urls")),
]
