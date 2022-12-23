from django.urls import path
from .views import tikets
urlpatterns = [
    path('', tikets),
]