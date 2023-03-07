from django.urls import path
from .views import ice_cream_view, index

app_name = 'icecream_app'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', ice_cream_view, name='ice_cream_view')
]
