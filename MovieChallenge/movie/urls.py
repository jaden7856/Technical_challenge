from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('movie.urls'), name='home'),
]
