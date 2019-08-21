from django.urls import path
from . import views

app_name='gallery'

urlpatterns = [
    path('', views.allPaintSty, name='allPaintSty'),
    path('<slug:s_slug>/', views.allPaintSty, name='paintings_by_style'),
]