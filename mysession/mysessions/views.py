from django.shortcuts import render


def set_session(request):
    
    request.session["first_name"] = "Arunesh"
    request.session["last_name"] = "thakur"
    
    # request.session.set_expiry(60)
    
    #!      test  cookies
    request.session.set_test_cookie()
    
    return render(request=request, template_name="mysessions/set-session.html")


def get_session(request):
    
    #!      get all values
    first_name = request.session.get("first_name")
    last_name = request.session["last_name"]
    
    # city = request.session["city"]
    # city = request.session.get("city")
    city = request.session.get("city", default="Guest")
    
    #!      keys()   items()        setdefault()
    print(request.session.keys())
    print(request.session.items())
    age = request.session.setdefault("age", "25")
    
    #!      others method
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    
    
    #!      test  cookies
    print(request.session.test_cookie_worked())
    
    context = {
        "last_name": last_name,
        "first_name": first_name,
        "city": city,
        "age": age
    }
    
    return render(request=request, template_name="mysessions/get-session.html", context=context)


def del_session(request):    
    #!      delete single item
    # if "first_name" in request.session:
    #     del request.session["first_name"]
    
    #!      delete all session
    # if "first_name" in request.session:
    #     # del request.session
    
    # request.session.flush()
    
    #!      clear expired sessions
    request.session.clear_expired()
    
    
    #!      test  cookies
    request.session.delete_test_cookie()
    
    
    return render(request=request, template_name="mysessions/del-session.html")



def bank_page(request):
    """
        auto reset time when page reload
    """
    
    if "first_name" in request.session:
        first_name = request.session["first_name"]
        
        request.session.modified = True
    else:
        first_name = None
        
    context={
        "first_name": first_name
    }
    
    return render(request=request, template_name="mysessions/bank.html", context=context)