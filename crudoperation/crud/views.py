from django.shortcuts import render, redirect

from crud.forms import StudentForm
from crud.models import Student



def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect("home")
        
    else:
        form = StudentForm()
    
    students = Student.objects.all()
    
    context = {
        "form": form,
        "students": students
    }
    
    return render(request=request, template_name="crud/home.html", context=context)