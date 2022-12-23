from django.shortcuts import render

# Create your views here.


def index(request) -> render:
    template_ = 'index.html'

    context = {}

    return render(request, template_, context=context)