from django.forms import ModelForm
from.models import Movie

class MovieForms(ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'rating', 'description', 'director',)