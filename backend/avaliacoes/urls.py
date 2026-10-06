from django.urls import path
from .views import listar_avaliacoes, listar_pendentes

urlpatterns = [
    path('', listar_avaliacoes),
    path('pendentes/', listar_pendentes),
]