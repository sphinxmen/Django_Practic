from django.shortcuts import render

# Create your views here.

def login_view(request) -> render:
    template_name = 'login_form.html'
    context = {}

    return render(request=request, template_name=template_name, context=context)