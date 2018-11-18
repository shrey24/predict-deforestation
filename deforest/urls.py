from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gis-home'),
    path('about/', views.about, name='gis-about'),
]