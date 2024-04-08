from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/ficha/<int:id_ficha>', views.fichadetalhes, name='detalhes'),
    path('update/<int:pk>', views.update, name='update'),
]