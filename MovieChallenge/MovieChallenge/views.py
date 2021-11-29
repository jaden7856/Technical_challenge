from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from movie.models import Movie

class HomeView(TemplateView):
    template_name = 'index.html'


@method_decorator(csrf_exempt)
def form_valid(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        #print(title)

        movie = Movie.objects.filter(title__contains=title)
        context = {'movie': movie}

        return render(request, 'search.html', context)
