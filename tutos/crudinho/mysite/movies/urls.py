from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path( '', views.FilmListView.as_view(), name = 'list' ),
    path( 'film/<int:pk>/detail/', views.FilmDetailView.as_view(), name = 'detail' ),
    path( 'film/create/', views.FilmCreateView.as_view(), name = 'create' ),
    path( 'film/<int:pk>/update/', views.FilmUpdateView.as_view(), name = 'update' ),    
    path( 'film/<int:pk>/delete/', views.FilmDeleteView.as_view(), name = 'delete' ),
    path( 'cringe/', views.test_cringe, name = 'cringe' ),
]
    
