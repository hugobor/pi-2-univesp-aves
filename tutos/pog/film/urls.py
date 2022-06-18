from django.urls import path
from . import views

app_name = 'film'

urlpatterns = [
    path( '', views.FilmListView.as_view(), name= 'film_list' ),
]
