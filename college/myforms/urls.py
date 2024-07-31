from django.urls import path

from myforms.views import my_forms, form_example, style_form_view


urlpatterns = [
    path("my-forms/", view=my_forms, name="my_forms"),
    path("form-examples/", view=form_example, name="form_example"),
    path("style-form/", view=style_form_view, name="style_form_view"),
]
