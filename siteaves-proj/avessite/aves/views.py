from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy

from .models import Ave

from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views import View

from django.contrib.messages.views import SuccessMessageMixin

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetView, NamedFormsetsMixin


class AveView( View ):
    """View de aves. Para não ter que por o Model em todas as views normais."""
    model = Ave


class AveListView( AveView, ListView ):
    #template='ave/ave_list.html'
    pass


class AveCreateView( NamedFormsetsMixin, SuccessMessageMixin, AveView, CreateWithInlinesView ):
    #template='ave/ave_form.html'
    success_message = "Ave %(nome)s foi inclúida com sucesso!"
    success_url = ""
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

        
               

