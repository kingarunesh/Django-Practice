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


def edit_student(request, id):
    
    student = Student.objects.get(pk=id)
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        
        if form.is_valid():
            form.save()
            
            return redirect("home")
        
    else:
        form = StudentForm(instance=student)
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="crud/update.html", context=context)


def delete_student(request, id):
    student = Student.objects.get(pk=id)
    
    student.delete()
    
    return redirect("home")