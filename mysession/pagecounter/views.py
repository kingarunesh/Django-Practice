from django.shortcuts import render


def page_counter(request):
    
    total = request.session.get("count", default=0)
    
    new_count = total + 1
    
    request.session["count"] = new_count
    
    context = {
        "count": total + 1
    }
    
    return render(request=request, template_name="pagecounter/counter.html", context=context)