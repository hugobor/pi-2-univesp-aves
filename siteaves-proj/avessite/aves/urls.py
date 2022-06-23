from django.urls import path

from . import views

from django.views.generic import RedirectView
from django.urls import reverse_lazy

app_name = 'aves'

urlpatterns = [
    path( '',RedirectView.as_view( url = reverse_lazy( 'aves:ave_list' )), name = 'index' ),
    path( 'hello/', views.hello, name = 'hello' ),
    path( 'ave_list/', views.AveListView.as_view(), name = 'ave_list' ),
    path( 'ave/create/', views.AveCreateView.as_view(), name = 'ave_create' ),
]
