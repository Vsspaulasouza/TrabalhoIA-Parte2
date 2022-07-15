from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



#DEFINIÇÃO DA VARIAVEL PARA REFERENCIA
app_name="home"

urlpatterns = [
    path('', views.index),   
    path('cadastro', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]