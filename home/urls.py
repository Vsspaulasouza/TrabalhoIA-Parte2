from django.urls import path
from . import views

#DEFINIÇÃO DA VARIAVEL PARA REFERENCIA
app_name="home"

urlpatterns = [
    path('', views.index),
]