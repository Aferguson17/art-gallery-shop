from django.urls import path
from . import views

app_name='search_application'

urlpatterns = [
    path('', views.searchResults, name='searchResults'),
]