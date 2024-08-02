from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from first.forms import RegisterForm



def register(request):
    
    #NOTE :         we can do also like this
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
            
    # else:
    #     form = UserCreationForm()
    
    #NOTE :         custom form edit
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Account Register successfully...")
            
    else:
        form = RegisterForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/register.html", context=context)