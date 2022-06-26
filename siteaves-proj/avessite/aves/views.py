from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy

from .models import Ave, InfoExtra, FotoAve

from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views import View

from django.contrib.messages.views import SuccessMessageMixin

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetView, NamedFormsetsMixin, NamedFormsetsMixin, InlineFormSetFactory


class AveView( View ):
    """View de aves. Para não ter que por o Model em todas as views normais."""
    model = Ave


class AveListView( AveView, ListView ):
    #template='ave/ave_list.html'
    pass


class AveDetailView( AveView, DetailView ):
    #template='ave/ave_detail.html'
    pass


class InfoExtraInline( InlineFormSetFactory ):
    model = InfoExtra
    fields = '__all__'

class FotoAveInline( InlineFormSetFactory ):
    model = FotoAve
    fields = '__all__'


class AveCreateView( NamedFormsetsMixin, SuccessMessageMixin, AveView, CreateWithInlinesView ):
    #template='ave/ave_form.html'
    success_message = "Ave %(nome_cientifico)s foi inclúida com sucesso!"
    success_url = reverse_lazy( 'aves:ave_list' )
    fields = (
        'nome_cientifico',
        'autor',
        'nome_popular',
        'nome_ingles',
        'familia',
        'imagem_capa',
        'estado_iucn_sp',
        'estado_iucn_int',
        'frequencia_ocorrencia',
        'abundancia_relativa',
        'info',
    )
    inlines = [ InfoExtraInline, FotoAveInline ]
    inlines_names = [ 'infoextra_inline', 'fotoave_inline' ]



        
        


class AveEditView( NamedFormsetsMixin, SuccessMessageMixin, AveView, UpdateWithInlinesView ):
    #template='ave/ave_form.html'
    success_message = "Ave %(nome_cientifico)s foi editada com sucesso!"
    success_url = reverse_lazy( 'aves:ave_list' )
    fields = (
        'nome_cientifico',
        'autor',
        'nome_popular',
        'nome_ingles',
        'familia',
        'imagem_capa',
        'estado_iucn_sp',
        'estado_iucn_int',
        'frequencia_ocorrencia',
        'abundancia_relativa',
        'info',
    )
    inlines = [ InfoExtraInline, FotoAveInline ]
    inlines_names = [ 'infoextra_inline', 'fotoave_inline' ]
    

        
               

