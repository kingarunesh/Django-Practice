from django.urls import path
from django.views.decorators.cache import cache_page

from perview.views import first_view, second_view, third_view


urlpatterns = [
    path("first/", view=first_view),
    
    path("second/", cache_page(timeout=20)(second_view)),
    path("second/second/", view=second_view),
    
    path("third/", view=third_view),
]
