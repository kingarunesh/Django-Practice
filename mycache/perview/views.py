from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(timeout=15)
def first_view(request):
    return render(request=request, template_name="perview/first.html")


def second_view(request):
    return render(request=request, template_name="perview/second.html")


def third_view(request):
    return render(request=request, template_name="perview/third.html")