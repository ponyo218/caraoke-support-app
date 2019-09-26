from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_song, name='all_song'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('iTunes_search/', views.iTunes_search, name='iTunes_search'),
    path('song/<int:pk>/scraping/', views.scraping, name='scraping'),
]