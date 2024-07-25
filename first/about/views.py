from django.shortcuts import render
from django.http import HttpResponse


def my_about(request):
    return HttpResponse("<h1>My About - About APP</h1>")