from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ficha/<int:id_ficha>', views.fichadetalhes, name='detalhes'),
]