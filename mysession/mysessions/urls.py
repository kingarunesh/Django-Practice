from django.urls import path

from mysessions.views import del_session, get_session, set_session


urlpatterns = [
    path("set-session/", view=set_session),
    path("get-session/", view=get_session),
    path("del-session/", view=del_session),
]
