from django.urls import path

from mycookies.views import set_cookies, get_cookies, delete_cookies


urlpatterns = [
    path("set-cookies/", view=set_cookies),
    path("get-cookies/", view=get_cookies),
    path("delete-cookies/", view=delete_cookies),
]
