from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy

from .models import Ave, InfoExtra, FotoAve, Familia, Ordem, ClassifiExtra

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.views import View

from django.contrib.messages.views import SuccessMessageMixin

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetView, NamedFormsetsMixin, NamedFormsetsMixin, InlineFormSetFactory, SearchableListMixin



# Aves
class AveView( View ):
    """View de aves. Para não ter que por o Model em todas as views normais."""
    model = Ave


class AveListView( SearchableListMixin, AveView, ListView ):
    #template='ave/ave_list.html'
    search_fields = [ 'nome_cientifico', 'nome_popular' ]
    pass


class AveDetailView( AveView, DetailView ):
    #template='ave/ave_detail.html'
    pass


class AveDeleteView( SuccessMessageMixin, AveView, DeleteView ):
    #template='ave/ave_confirm_delete.html'
    success_url = reverse_lazy( 'aves:ave_list' )

    def get_success_message( self, cleaned_data ):
        """Gambiarra para retornar mensagem de sucesso com o objeto já exclúido."""
        return f"Ave \"{self.object}\" foi removida com sucesso!"
    

class InfoExtraInline( InlineFormSetFactory ):
    model = InfoExtra
    fields = '__all__'


class FotoAveInline( InlineFormSetFactory ):
    model = FotoAve
    fields = '__all__'


class AveCreateView( NamedFormsetsMixin, SuccessMessageMixin, AveView, CreateWithInlinesView ):
    #template='ave/ave_form.html'
    success_message = "Ave \"%(nome_cientifico)s\" foi inclúida com sucesso!"
    #success_url = reverse_lazy( 'aves:ave_list' )
    #success_url = reverse( 'aves:ave_detail' ...
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
    success_message = "Ave \"%(nome_cientifico)s\" foi editada com sucesso!"
    #success_url = reverse_lazy( 'aves:ave_list' )
    #success_url = reverse( 'aves:ave_detail' ...    
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
    

        


#Taxonomia
class FamiliaInLine( InlineFormSetFactory ):
    model = Familia
    fields = '__all__'
    factory_kwargs = { 'extra': 20 }

    
class OrdemView( View ):
    model = Ordem


class OrdemListView( OrdemView, ListView ):
    #template='ave/ordem_list.html'
    pass


class OrdemCreateView( NamedFormsetsMixin, SuccessMessageMixin, OrdemView, CreateWithInlinesView ):
    #template='ave/ordem_form.html'
    success_message = "Ordem \"%(nome)s\" foin incúida com sucesso!"
    success_url = reverse_lazy( 'aves:ordem_list' )
    fields = '__all__'
    inlines = [ FamiliaInLine ]
    inlines_names = [ 'familia_inline' ]


class OrdemEditView( NamedFormsetsMixin, SuccessMessageMixin, OrdemView, UpdateWithInlinesView ):
    success_message = "Ordem \"%(nome)s\" foi editada com sucesso!"
    success_url = reverse_lazy( 'aves:ordem_list' )
    fields = '__all__'
    inlines = [ FamiliaInLine ]
    inlines_names = [ 'familia_inline' ]    
    


class OrdemDeleteView( SuccessMessageMixin, OrdemView, DeleteView ):
    #template='ave/ordem_confirm_delete.html'
    success_url = reverse_lazy( 'aves:ordem_list' )

    def get_success_message( self, cleaned_data ):
        return f"Ordem \"{self.object}\" foi removida com sucesso!"


#ClassifiExtra
class ClassifiExtraView( View ):
    model = ClassifiExtra

class ClassifiExtraListView( ClassifiExtraView, ListView ):
    #template='ave/classifiextra_list.html'
    pass

class ClassifiExtraCreateView( SuccessMessageMixin, ClassifiExtraView, CreateView ):
    #template='ave/classifiextra_form.html'
    def get_success_message( self, cleaned_data ):
        return f"Classificação \"{self.object}\" foi criada com sucesso!"        
    success_url = reverse_lazy( 'aves:classifi_list' )
    fields = '__all__'


class ClassifiExtraEditView( SuccessMessageMixin, ClassifiExtraView, UpdateView ):
    #template='ave/classifiextra_form.html'
    
    def get_success_message( self, cleaned_data ):
        return f"Classificação \"{self.object}\" foi editada com sucesso!"    

    success_url = reverse_lazy( 'aves:classifi_list' )
    fields = '__all__'
    

class ClassifiExtraDeleteView( SuccessMessageMixin, ClassifiExtraView, DeleteView ):
    #template='ave/ordem_confirm_delete.html'
    success_url = reverse_lazy( 'aves:classifi_list' )

    def get_success_message( self, cleaned_data ):
        return f"Classificação \"{self.object}\" foi removida com sucesso!"
    
