from django.urls import path

from . import views

from django.views.generic import RedirectView
from django.urls import reverse_lazy

app_name = 'aves'

urlpatterns = [
    path( '',RedirectView.as_view( url = reverse_lazy( 'aves:ave_list' )), name = 'index' ),
    path( 'ave_list/', views.AveListView.as_view(), name = 'ave_list' ),
    path( 'ave/create/', views.AveCreateView.as_view(), name = 'ave_create' ),
    path( 'ave/<int:pk>/edit/', views.AveEditView.as_view(), name = 'ave_edit' ),
    path( 'ave/<int:pk>/detail/', views.AveDetailView.as_view(), name = 'ave_detail' ),
]
