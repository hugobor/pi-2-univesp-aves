from django.urls import path

from . import views

app_name = 'gamu'

urlpatterns = [
    path( '', views.GameListView.as_view(), name = 'list' ),
    path( 'game/<int:pk>/detail/', views.GameDetailView.as_view(), name = 'detail' ),
    path( 'game/create/', views.GameCreateView.as_view(), name = 'create' ),    
    
]
