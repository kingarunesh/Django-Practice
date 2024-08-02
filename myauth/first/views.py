from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages

from first.forms import RegisterForm, EditProfileForm, EditAdminProfileForm



def register(request):
    
    if request.user.is_authenticated:
        return redirect("profile_view")
    
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


def login_view(request):
    
    if request.user.is_authenticated:
        return redirect("profile_view")
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request=request, user=user)
                
                messages.success(request, "Login success...")
                
                return redirect("profile_view")
    else:
        form = AuthenticationForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/login.html", context=context)


def profile_view(request):
    
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    if request.method == "POST":
        
        if request.user.is_superuser:
            form = EditAdminProfileForm(request.POST, instance=request.user)
        else:
            form = EditProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Profile Updated...")
            
    else:
        if request.user.is_superuser:
            form = EditAdminProfileForm(instance=request.user)
        else:
            form = EditProfileForm(instance=request.user)
    
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users = None
    
    context = {
        "user_details": request.user,
        "form": form,
        "users": users
    }
    
    return render(request=request, template_name="first/profile.html", context=context)

def user_details(request, id):
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    if not request.user.is_superuser:
        return redirect("profile_view")
    
    user_info = User.objects.get(pk=id)
    
    if request.method == "POST":
        form = EditAdminProfileForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success("Updated")
    else:
        form = EditAdminProfileForm(instance=user_info)
    
    context = {
        "user_info": user_info,
        "form": form
    }
    
    return render(request=request, template_name="first/user-details.html", context=context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    logout(request=request)
    
    return redirect("login_view")


def change_password(request):
    
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Password updated")
            # return redirect("login_view")
            
            #!      it will not logout and update current session with new password
            update_session_auth_hash(request=request, user=form.user)
            return redirect("profile_view")
            
        
    else:
        form = PasswordChangeForm(user=request.user)
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/change-password.html", context=context)


def change_password_without_old_pass(request):
    
    if not request.user.is_authenticated:
        return redirect("login_view")
    
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Password updated")
            # return redirect("login_view")
            
            #!      it will not logout and update current session with new password
            update_session_auth_hash(request=request, user=form.user)
            return redirect("profile_view")
            
        
    else:
        form = SetPasswordForm(user=request.user)
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="first/pass-change-without-old-pass.html", context=context)