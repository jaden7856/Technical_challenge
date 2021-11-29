from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render
from django.http import HttpResponse
from movie.models import *


class MovieList(ListView):
    template_name = "movieList.html"

    def movie_list(request):
        data = Movie.objects.all()

        movies = { "object_list" : data }
        return render(request, "movieList.html", movies)


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