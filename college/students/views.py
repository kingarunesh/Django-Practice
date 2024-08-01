from django.shortcuts import render, redirect

from students.models import Student
from students.forms import StudentForm


def students(request):
    
    students = Student.objects.all()
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            #!      1
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            data = Student(name=name, email=email, password=password)
            data.save()
            
            #!      2 
            # form.save()

            return redirect("students")
            
    else:
        form = StudentForm()
    
    
    context = {
        "students": students,
        "form": form
    }
    
    return render(request=request, template_name="students/students.html", context=context)