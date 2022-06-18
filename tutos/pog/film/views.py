from django.shortcuts import render

from django.views import View
from django.views.generic.list import ListView

from django.urls import reverse_lazy

from .models import Filme

class FilmBaseView( View ):
    model = Filme
    fields = '__all__'
    success_url = reverse_lazy( 'film:film_list' )


class FilmListView( FilmBaseView, ListView ):
    pass
