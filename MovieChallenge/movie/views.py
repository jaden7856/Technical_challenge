from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
#from config import Config
from movie.models import *




def movie_list(request):
    movies = Movie.objects.all()

    return render(request, "movieList.html", {"movies" : movies})


class movieDetail(DetailView):
    template_name = "movieDetail.html"


class movieReviewList(ListView):

    def movie_review_create(request):
        # return HttpResponse("movieReviewCreate")
        return render(request, '')

    def movie_review_remove(request):
        # return HttpResponse("movieReviewRemove")
        return render(request, '')

    def movie_review_edit(request):
        # return HttpResponse("movieReviewEdit")
        return render(request, '')


def movie_review_vote_create(request):
    # return HttpResponse("movieReviewVoteCreate")
    return render(request, '')

def movie_review_vote_remove(request):
    # return HttpResponse("movieReviewVoteRemove")
    return render(request, '')