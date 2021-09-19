import requests
import json


def pesquisar(palavraChave, order):
    apiKey = "AIzaSyCUVcai7yzkeQrN-yeabuKga1nd4-5Cvpg"

    url = f"https://youtube.googleapis.com/youtube/v3/search?part=id&maxResults=1&order={order}&publishedAfter=2010-01-01T00%3A00%3A00Z&q={palavraChave}&regionCode=BR&type=video&videoEmbeddable=true&key={apiKey}"

    videoId = requests.get(url).json()["items"][0]["id"]["videoId"]
    resposta = f'<iframe width="250" height="150" src="https://www.youtube.com/embed/{videoId}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    return resposta
