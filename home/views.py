import re
from django.http.response import HttpResponseBase, HttpResponseGone, HttpResponseNotModified, JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from home.aiml.cria_respostas import bot
from home.YouTube.pesquisarporpalavrachave import pesquisar
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginDjango
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login/')
def enviaMsg(request):
    if request.method == 'POST':
        mensagem = request.POST.get('entrada')
        resposta = bot.geraResposta(mensagem)
        if resposta.endswith(".youtube"):
            resposta = resposta.replace(".youtube", "")
            order = resposta.partition(".")[2]
            order = order.replace(" ", "")
            order = order.replace(".", "")
            resposta = resposta.replace(f".{order}", "")
            resposta = resposta.replace(" ", "%20")
            resposta = pesquisar(resposta, order)
    return JsonResponse({'resposta': resposta})


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:            
            messages.info(request, 'Ja existe um usuario com esse Login!!')
            return redirect('/cadastro')

        else:            
            user = User.objects.create_user(username=username, email=email, password=senha)
            messages.info(request, 'Usuario cadastrado com sucesso')
            return redirect('/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            loginDjango(request, user)
            return render(request, 'politica.html')          
                