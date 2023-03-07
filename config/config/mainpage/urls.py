from django.urls import path
from .views import mainpage_view

app_name = "mainpage"

urlpatterns = [
    path('', mainpage_view, name='mainpage_view')
]