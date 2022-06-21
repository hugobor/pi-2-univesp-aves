from django.shortcuts import render, reverse, redirect

from django.views.generic import ListView, DetailView, CreateView
from django.views import View
# Create your views here.

from .models import Game, DescricaoExtra, Console, ScreenShot

from .forms import DescricaoFormSet, ScreenShotFormSet


def hello( request ):
    return render( request, 'gamu/hello.html' )

class GameView( View ):
    model = Game

class GameListView( GameView, ListView ):
    pass

class GameDetailView( GameView, DetailView ):
    pass

class GameCreateView( GameView, CreateView ):
    fields = '__all__'

    def get_context_data( self, **kwargs ):
        context = super().get_context_data( **kwargs )
        context[ 'descricao_extra_formset' ] = DescricaoFormSet()
        context[ 'screenshot_formset' ] = ScreenShotFormSet()

        return context

    def post( self, request, *args, **keyargs ):
        self.object = None
        form = self.get_form( self.get_form_class() )
        
        descricao_extra_formset = DescricaoFormSet( self.request.POST )
        screenshot_formset = ScreenShotFormSet( self.request.POST )
        print( screenshot_formset )
        if form.is_valid() and descricao_extra_formset.is_valid() and screenshot_formset.is_valid():
            return self.blip_form_valid( form, descricao_extra_formset, screenshot_formset )
        else:
            return self.blip_form_invalid( form, descricao_extra_formset, screenshot_formset )            

    def blip_form_valid( self, form, descricao_extra_formset, screenshot_formset ):
        self.object = form.save()
        descrs = descricao_extra_formset.save( commit = False )
        for descr in descrs:
            descr.game = self.object
            descr.save()
        scrs = screenshot_formset.save( commit = False )
        print( "FIFLDkFDSJLKFLJLKFDSLÇ" )
        print( scrs )
        print( "FIFLDkFDSJLKFLJLKFDSLÇ" )
        print( self.request.POST )
        print( self.request.FILES )
        print( "FIFLDkFDSJLKFLJLKFDSLÇ" )        
        

        for scr in scrs:
            scr.game = self.object
            scr.save()

        return redirect( reverse( 'gamu:detail', args=( self.object.pk ,)))

    def blip_form_invalid( self, form, descricao_extra_formset, screenshot_formset ):
        return self.render_to_response(
            self.get_context_data( form = form,
                                   descricao_extra_formset = descricao_extra_formset,
                                   screenshot_formset = screenshot_formset ))
                                   
                                                     
        

    
