from django.urls import path  # type: ignore
from . import views

# /movies
# /movies/1/details

# map view to url

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
