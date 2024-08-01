from django.shortcuts import render

from first.models import Aohan
from first.forms import AohanForm


def first_view(request):
    if request.method == "POST":
        form = AohanForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    else:
        form = AohanForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/first.html", context=context)