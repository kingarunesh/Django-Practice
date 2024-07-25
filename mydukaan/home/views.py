from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        "title": "Home Page",
        "heading": "Complete Django",
        "body": "This is body TEXT",
        "current_date_time": datetime.now()
    }
    
    return render(request=request, template_name="home/index.html", context=context)


def about(request):
    return render(request=request, template_name="home/about.html")