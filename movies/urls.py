from django.urls import path  # type: ignore
from . import views

# /movies
# /movies/1/details

# map view to url
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail')
]
