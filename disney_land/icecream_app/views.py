from django.shortcuts import render
from .models import Ice_cream_shop
# Create your views here.


def index(request) -> render:
    """ Вывод данных из таблицы Movie отсортированных
        по убыванию по полю pk
    """
    template_ = 'index.html'
    kiosks = Ice_cream_shop.objects.all()

    ice_creams = Ice_cream_shop.objects.all()
    context = {'kiosk': kiosks,
               'ice_creams': ice_creams
               }

    return render(request, template_, context=context)

def ice_cream_view(request, pk) -> render:
    template_ = 'shop.html'
    current_ice_cream = Ice_cream_shop.objects.get(pk=pk)

    ice_creams = Ice_cream_shop.objects.all()

    context = {
        'current_ice_cream': current_ice_cream,
        'ice_creams': ice_creams
    }
    return render(request, template_, context=context)