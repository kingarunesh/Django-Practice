"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from school import views
from college import views as clg
from contact import views as cl


contact_url_path = [
    path("my-contact/", view=cl.my_contact)
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=views.index),
    path("about/", view=views.about),
    path("contact/", view=views.contact),
    path("service/", view=views.service),
    path("my-math/", view=views.my_math),
    path("branch/", view=clg.branch),
    
    path("others/", include("about.urls")),
    
    # path("other-contact/", include([
    #     path("my-contact/", view=cl.my_contact)
    # ]))
    path("other-contact/", include(contact_url_path))
]
