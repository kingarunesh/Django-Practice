from django.urls import path

from mysessions.views import del_session, get_session, set_session, bank_page


urlpatterns = [
    path("set-session/", view=set_session),
    path("get-session/", view=get_session),
    path("del-session/", view=del_session),
    path("bank/", view=bank_page),
]
