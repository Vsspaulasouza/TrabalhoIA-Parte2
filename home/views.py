import re
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
            order = resposta.partition(".")[2]
            order = order.replace(" ", "")
            order = order.replace(".", "")
            resposta = resposta.replace(f".{order}", "")
            resposta = resposta.replace(" ", "%20")
            resposta = pesquisar(resposta, order)
    return JsonResponse({'resposta': resposta})
