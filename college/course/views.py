from django.shortcuts import render

from course.models import Course


def course(request):
    
    course_list = Course.objects.all()
    
    first_course = Course.objects.get(pk=1)
    
    context = {
        "course_list": course_list,
        "first_course": first_course
    }
    
    return render(request=request, template_name="course/course.html", context=context)