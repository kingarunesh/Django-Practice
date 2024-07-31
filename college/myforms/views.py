from django.shortcuts import render

from myforms.forms import FirstForm, SecondForm, ExampleForm, StyleForm



def my_forms(request):
    #!      1
    # form = FirstForm()
    
    #!      2
    # form = FirstForm(auto_id="some_%s")
    # form = FirstForm(auto_id="%s")
    # form = FirstForm(auto_id=True)
    # form = FirstForm(auto_id=False)
    
    #!      3
    # form = FirstForm(auto_id=True)
    # form = FirstForm(auto_id=True, label_suffix="")
    # form = FirstForm(auto_id=True, label_suffix=" ")
    # form = FirstForm(auto_id=True, label_suffix="-")
    
    #!      4
    # form = FirstForm(auto_id=True, label_suffix=" ", initial={"name": "King", "contact_number": "+91 8971818410"})
    
    #!      5
    # form = FirstForm(auto_id=True, label_suffix=" ")
    # form.order_fields(field_order=None)  #^  default
    # form.order_fields(field_order=["contact_number", "email", "name"])
    
    #!      6
    form = SecondForm()
    
        
    context = {
        "form": form
    }
    
    return render(request=request, template_name="myforms/myforms.html", context=context)



def form_example(request):
    
    if request.method == "POST":
        form = ExampleForm(request.POST)
        
        if form.is_valid():
            # print(f"Name: {form.cleaned_data["name"]}.")
            # print(form.cleaned_data)
            
            for key in form.cleaned_data:
                print(f"{key} : {form.cleaned_data[key]}")
            
        
    else:
        form = ExampleForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="myforms/form-examples.html", context=context) 



def style_form_view(request):
    if request.method == "POST":
        form = StyleForm(request.POST)
        
        if form.is_valid():
            print(f"\n{form.cleaned_data}\n")
        
    else:
        form = StyleForm()
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="myforms/style-form.html", context=context)