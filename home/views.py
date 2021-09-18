from django.http.response import HttpResponseBase, HttpResponseGone, HttpResponseNotModified, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from home.aiml.cria_respostas import bot
from home.YouTube.pesquisarporpalavrachave import pesquisar
# Create your views here.


def index(request):
    return render(request, 'index.html')


def enviaMsg(request):
    if request.method == 'POST':
        mensagem = request.POST.get('entrada')
        resposta = bot.geraResposta(mensagem)
        if resposta.endswith(".youtube"):
            resposta = resposta.replace(".youtube", "")
            resposta = pesquisar(resposta)
    return JsonResponse({'resposta': resposta})
