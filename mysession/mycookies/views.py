from django.shortcuts import render

from datetime import datetime, timedelta, timezone


def set_cookies(request):
    response =  render(request=request, template_name="mycookies/set-cookies.html")
    
    #NOTE :         normal cookies set
    # response.set_cookie(key="first_name", value="Arunesh", max_age=10)
    # response.set_cookie(key="first_name", value="Arunesh", expires=datetime.now(timezone.utc) + timedelta(days=10))
    
    #NOTE :         signed cookies set
    response.set_signed_cookie(key="last_name", value="kumar", salt="aruneshthakur")
    
    return response


def get_cookies(request):
    
    #NOTE :         without signed cookie access
    # my_cookie = request.COOKIES["first_name"]
    
    #!      default value if value not exits
    # my_cookie = request.COOKIES.get("first_name", "Guest")
    
    #NOTE :         access signed cookies
    
    my_cookie = request.get_signed_cookie("last_name", salt="aruneshthakur", default="Guest")
    
    
    return render(request=request, template_name="mycookies/get-cookies.html", context={"my_cookie": my_cookie})


def delete_cookies(request):
    response =  render(request=request, template_name="mycookies/delete-cookies.html")
    
    # response.delete_cookie("first_name")
    response.delete_cookie("last_name")
        
    return response