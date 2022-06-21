from django.shortcuts import render, reverse
from django.views import View, generic
from django.urls import reverse_lazy

from django.http import HttpResponse

from .models import Film, Genre, Gamu, Console

from django.shortcuts import get_object_or_404

def test_cringe( request ):
    return render( request, 'movies/cringe.html', { 'gamu_list': Gamu.objects.all() })

class FilmView( View ):
    model = Film
    

class FilmListView( FilmView, generic.ListView ):
    template_name = 'movies/list.html'


class FilmDetailView( FilmView, generic.DetailView ):
    template_name = 'movies/detail.html'


class FilmCreateView( FilmView, generic.CreateView ):
    template_name = 'movies/edit.html'
    fields = '__all__'
    
    def get_success_url( self ):
        return reverse( 'movies:detail',
                        args = ( self.object.id ,))


class FilmUpdateView( FilmView, generic.UpdateView ):
    template_name = 'movies/edit.html'
    fields = '__all__'

    def get_success_url( self ):
        return reverse( 'movies:detail',
                        args = ( self.object.id ,))

class FilmDeleteView( FilmView, generic.DeleteView ):
    template_name = 'movies/confirm_delete.html'
    success_url = reverse_lazy( 'movies:list' )


    





    


