from django.shortcuts import render
from .forms import ModelForm
# from django.template import loader
# from django.http import (HttpResponse,)
from django.views.generic.edit import CreateView

from .models import Movie, Director


# Create your views here.

# def index(request) -> HttpResponse:
#     """ Вывод данных из таблицы Movie отсортированных 
#         по убыванию по полю pk
#     """
#     response_ = "Список фильмов c рейтингом в фильмотеке \r\n\r\n"
#     for item_movie in Movie.objects.order_by('-pk'):
#         response_ += item_movie.name + '\r\n'+ str(item_movie.rating) + '%\r\n'

#     return HttpResponse(response_, content_type='text/plain; charset=utf8')

# def index(request) -> HttpResponse:
#     """ Вывод данных из таблицы Movie отсортированных 
#         по убыванию по полю pk
#     """
#     template_ = loader.get_template('index.html')
#     movies = Movie.objects.order_by('-pk')
#     context = {'movies': movies}

#     return HttpResponse(template_.render(context, request))

class MovieCreateView(CreateView):
    model = Director
    form_class = ModelForm
    template_name = 'create_movie.html'
    success_url = '/'

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context['directors'] = Director.objects.all()
        return context


def index(request) -> render:
    """ Вывод данных из таблицы Movie отсортированных 
        по убыванию по полю pk
    """
    template_ = 'index.html'
    directors = Director.objects.all()
    movies = Movie.objects.order_by('-pk')

    context = {'movies': movies,
               'directors': directors}

    return render(request, template_, context=context)


def by_director(request, director_pk) -> range:
    template_ = "by_director.html"
    movies = Movie.objects.filter(director=director_pk)
    curent_dector = Director.objects.get(pk=director_pk)

    director = Director.objects.all()

    context = {
        'movies': movies,
        'curent_director': curent_dector,
        'director': director
    }
    return render(request, template_, context=context)



