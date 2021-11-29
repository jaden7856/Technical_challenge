from django.shortcuts import render
from django.http import HttpResponse


def movieCreate(request):
    # return HttpResponse("movieCreate")
    return render(request, '')

def movieReviewDetail(request):
    # return HttpResponse("movieReviewDetail")
    return render(request, '')

def movieReviewCreate(request):
    # return HttpResponse("movieReviewCreate")
    return render(request, '')

def movieReviewRemove(request):
    # return HttpResponse("movieReviewRemove")
    return render(request, '')

def movieReviewEdit(request):
    # return HttpResponse("movieReviewEdit")
    return render(request, '')

def movieReviewVoteCreate(request):
    # return HttpResponse("movieReviewVoteCreate")
    return render(request, '')

def movieReviewVoteRemove(request):
    # return HttpResponse("movieReviewVoteRemove")
    return render(request, '')