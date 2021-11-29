from django.urls import path, include
from . import views

app_name = 'movie'

urlpatterns = [
    # /movie/
    path('', views.MovieList.as_view(), name='movie_list'),
    # /movie/{id}/
    #path('/<int:movie_id>/', views.movieDetail.as_view(), name='movie_detail'),
    # /movie/reviews/
    path('review/', views.movieReviewList.as_view(), name="movie_review"),
]
