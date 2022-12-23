from django.shortcuts import render
from .models import Tikets


# Create your views here.

def tikets(request) -> render:
    """Вывод данных из таблицы Tikets отсортированных по убыванию"""
    template_ = 'tikets.html'
    tickets = Tikets.objects.order_by('-pk')
    context = {
        'tickets': tickets
    }
    return render(request, template_, context=context)
