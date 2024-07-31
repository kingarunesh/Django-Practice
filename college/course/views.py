from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from course.models import Course
from course.forms import CourseForm


def course(request):
    
    course_list = Course.objects.all()
    
    first_course = Course.objects.get(pk=1)
    
    if request.method == "POST":
        forms = CourseForm(request.POST)
        
        if forms.is_valid():
            # print(forms.clean())
            # print(forms.full_clean())
            # print(forms.cleaned_data)
            # print(forms.cleaned_data["title"])
            
            print(f"TITLE: {forms.cleaned_data["title"]}")
            print(f"DESCRIPTION: {forms.cleaned_data["description"]}")
            print()
            #!      This is not good way
            # print(f"TITLE: {request.POST["title"]}")
            # print(f"DESCRIPTION: {request.POST["description"]}")
            
            # return HttpResponseRedirect("/success/")
            # return redirect("success_submit", title= forms.cleaned_data["title"])
            # return redirect("success_submit", title="hello")
            return redirect("success_submit")
    else:
        forms = CourseForm()
    
    context = {
        "course_list": course_list,
        "first_course": first_course,
        "forms": forms
    }
    
    return render(request=request, template_name="course/course.html", context=context)


def success_submit(request):
    return render(request=request, template_name="course/success.html")