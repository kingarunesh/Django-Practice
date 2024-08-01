from django.shortcuts import render
from django.contrib import messages

from first.models import Aohan
from first.forms import AohanForm


def first_view(request):
    if request.method == "POST":
        form = AohanForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            #!      long
            # messages.add_message(request, messages.SUCCESS, "Success -> Data Added to DataBase.")
            # messages.add_message(request, messages.INFO, "Info -> Data Added to DataBase.")
            
            #!      shortcut
            messages.success(request, "Success -> Data Added to DataBase...")
            messages.info(request, "Info -> Data Added to DataBase...")
    
    else:
        form = AohanForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/first.html", context=context)