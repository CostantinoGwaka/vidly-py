from django.urls import path  # type: ignore
from . import views

# /movies
# /movies/1/details

# map view to url
urlpatterns = [
    path('', views.index, name='index')
]
