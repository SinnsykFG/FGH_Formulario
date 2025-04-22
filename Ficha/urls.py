from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_view, name='formulario'),
    path('gracias/', views.agradecimiento_view, name='agradecimiento'),
    path('pacientes/', views.ver_pacientes_view, name='ver_pacientes'),
    path('buscar/', views.buscar_view, name='buscar'),
]
