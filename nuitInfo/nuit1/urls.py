from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Remplacez 'index' par votre vue réelle
]
