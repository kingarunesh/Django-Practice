from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index Page")

def about(request):
    return HttpResponse("<h1>Arunesh kumar</h1>")

def contact(request):
    data = "This is Contact Page"
    return HttpResponse(data)

def service(request):
    data = "Service"
    return HttpResponse(f"This is {data} page")

def my_math(request):
    a = 10
    b = 20
    return HttpResponse(f"{a} + {b} = {a + b}")