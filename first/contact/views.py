from django.shortcuts import render

from django.http import HttpResponse


def my_contact(request):
    return HttpResponse("My Contact Page")