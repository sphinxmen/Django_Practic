from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound,)
from django.views.generic.edit import CreateView



# Create your views here.


def go_to_page(request, string="this is a clinic blog") -> HttpResponse:
    return HttpResponse(string)


def index(request) -> render:
    template_ = 'index.html'

    context = {
        'string': "this is a clinic blog"
    }
    return render(request, template_, context=context)