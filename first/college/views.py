from django.shortcuts import render
from django.http import HttpResponse


def branch(request):
    return HttpResponse("College Branch")