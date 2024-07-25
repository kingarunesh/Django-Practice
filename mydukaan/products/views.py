from django.shortcuts import render


def themes(request):
    return render(request=request, template_name="products/themes.html")


def plugins(request):
    return render(request=request, template_name="products/plugins.html")