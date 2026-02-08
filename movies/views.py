from django.shortcuts import render  # type: ignore
from django.http import HttpResponse  # type: ignore
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
