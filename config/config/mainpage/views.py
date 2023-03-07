from django.shortcuts import render

# Create your views here.

def mainpage_view(request) -> render:
    template_name = 'mainpage_view.html'
    context = {}

    return render(request=request, template_name=template_name, context=context)