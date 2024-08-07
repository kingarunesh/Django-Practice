from django.shortcuts import render


def first_view(request):
    return render(request=request, template_name="tfcache/first.html")