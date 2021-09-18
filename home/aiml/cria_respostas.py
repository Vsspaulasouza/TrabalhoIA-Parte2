import aiml
from aiml.Kernel import Kernel


class Bot():
    def __init__(self):
        self.nucleo = aiml.Kernel()
        self.nucleo.learn("home/aiml/start.xml")
        self.nucleo.respond("carregar bot")

    def geraResposta(self, mensagem):
        return self.nucleo.respond(mensagem)


bot = Bot()
