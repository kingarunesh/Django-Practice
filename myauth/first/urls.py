from django.urls import path

from first.views import register, login_view, profile_view, logout_view, change_password, change_password_without_old_pass, user_details


urlpatterns = [
    path("register/", view=register, name="register"),
    path("login/", view=login_view, name="login_view"),
    path("profile/", view=profile_view, name="profile_view"),
    path("user-details/<int:id>/", view=user_details, name="user_details"),
    path("logout/", view=logout_view, name="logout_view"),
    path("change-password/", view=change_password, name="change_password"),
    path("change-password-1/", view=change_password_without_old_pass, name="change_password_without_old_pass"),
]
