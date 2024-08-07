from django.shortcuts import render
from django.http import HttpResponse

from django.core.cache import cache


def low_level_cache(request):
    
    #!          1 - method to set value and get
    movie_title = cache.get(key="movie", default="empty")
    
    if movie_title == "empty":
        cache.set(key="movie", value="FallOut", timeout=10)
    
    movie_title = cache.get(key="movie")
    
    #!          2 - set and get value
    first_name = cache.get_or_set("first_name", "Arunesh", 10)
    last_name = cache.get_or_set("last_name", "thakur", timeout=15, version=2)
    
    #!          3 - set & get many
    info = {
        "name": "Arunesh Thakur",
        "city": "Bangalore",
        "number": "8971818410"
    }
    
    cache.set_many(data=info, timeout=15)
    person_info = cache.get_many(info)
    
    #!          4 - delete cache
    cache.delete("first_name")
    cache.delete("last_name", version=2)
    
    
    context = {
        "movie_title": movie_title,
        "first_name": first_name,
        "last_name": last_name,
        "person_info": person_info
    }
    
    return render(request=request, template_name="lowlevelcache/lowlevelcache.html", context=context)


def delete_cache(request):
    cache.clear()
    return HttpResponse("<h1>Clear...</h1>")