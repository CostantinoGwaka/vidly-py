from django.shortcuts import render, get_object_or_404  # type: ignore
from django.http import HttpResponse, Http404  # type: ignore
from .models import Movies


# Create your views here.
def index(request):
    mov = Movies.objects.all()
    # output = ','.join([m.title for m in mov])
    # # select * from movies_movie
    # Movies.objects.filter(release_year=1984)
    # # select * from movies_movie
    # Movies.objects.get(id=1)
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': mov})


def detail(request, movie_id):

    #     try:
    #         mov = Movies.objects.get(pk=movie_id)
    #         return render(request, 'movies/detail.html', {'movie': mov})
    # # return HttpResponse(movie_id)
    #     except Movies.DoesNotExist:
    #         raise Http404()
    mov = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': mov})
    # return HttpResponse(movie_id)
