from django.shortcuts import render
from .models import Humans

# Create your views here.


# def person_view(request) -> render:
#     template_ = 'person.html'
#     person_view_ = Humans.objects.order_by('-pk')
#     context = {
#         'persons': person_view_
#     }
#     return render(request, template_, context=context)


def person_view(request, pk) -> render:
    template_ = 'person.html'
    current_person = Humans.objects.get(pk=pk)

    # if current_person.gender

    persons = Humans.objects.all()
    context = {
        'current_person': current_person,
        'persons': persons
    }
    return render(request, template_, context=context)