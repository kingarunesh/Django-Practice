from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    else:
        form = UserCreationForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/register.html", context=context)