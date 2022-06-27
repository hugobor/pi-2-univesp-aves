from django.urls import path

from . import views

from django.views.generic import RedirectView
from django.urls import reverse_lazy

app_name = 'aves'

urlpatterns = [
    path( '',RedirectView.as_view( url = reverse_lazy( 'aves:ave_list' )), name = 'index' ),

    #Aves
    path( 'ave_list/', views.AveListView.as_view(), name = 'ave_list' ),
    path( 'ave/create/', views.AveCreateView.as_view(), name = 'ave_create' ),
    path( 'ave/<int:pk>/edit/', views.AveEditView.as_view(), name = 'ave_edit' ),
    path( 'ave/<int:pk>/detail/', views.AveDetailView.as_view(), name = 'ave_detail' ),
    path( 'ave/<int:pk>/delete/', views.AveDeleteView.as_view(), name = 'ave_delete' ),

    #Ordem
    path( 'ordem/ordem_list/', views.OrdemListView.as_view(), name = 'ordem_list' ),
    path( 'ordem/create/', views.OrdemCreateView.as_view(), name = 'ordem_create' ),
    path( 'ordem/<int:pk>/edit/', views.OrdemEditView.as_view(), name = 'ordem_edit' ),    
    path( 'ordem/<int:pk>/delete/', views.OrdemDeleteView.as_view(), name = 'ordem_delete' ),

    #Classificação
    path( 'classifi/classifi_list/', views.ClassifiExtraListView.as_view(), name = 'classifi_list' ),
    path( 'classifi/create/', views.ClassifiExtraCreateView.as_view(), name = 'classifi_create' ),
    path( 'classifi/<int:pk>/edit/', views.ClassifiExtraEditView.as_view(), name = 'classifi_edit' ),    
    path( 'classifi/<int:pk>/delete/', views.ClassifiExtraDeleteView.as_view(), name = 'classifi_delete' ),
    
]
