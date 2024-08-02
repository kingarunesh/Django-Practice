from django.urls import path

from first.views import register, login_view, profile_view, logout_view


urlpatterns = [
    path("register/", view=register, name="register"),
    path("login/", view=login_view, name="login_view"),
    path("profile/", view=profile_view, name="profile_view"),
    path("logout/", view=logout_view, name="logout_view"),
]
