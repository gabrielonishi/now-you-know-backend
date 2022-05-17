"""
Arquivo criado para encapsulamento
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('api/<str:artist_name>/', views.api_artist),
    # path('api/artists/', views.api_artists_list),
    # path('api/tries/', views.api_user_tries_list),
    path('api/<str:artist_name>/tries/', views.api_artist_tries)
]