import telebot
import time
import dotenv
import os
from datetime import datetime



class Notificacao:
    def __init__(self, TOKEN):
        self.TOKEN = TOKEN
        

    def enviar_notificacao(self, mensagem):
        self.bot = telebot.TeleBot(self.TOKEN)
        self.bot.send_message(7021296280, mensagem)

'''
if __name__ == '__main__':

    while True:
        # Instancia
        notificacao = Notificacao(os.getenv("KEY"))

        # pega a hora do ponto
        hora_capturada = datetime.now().strftime("%H:%M:%S")
        
        # Envia a mensagem.
        mensagem = f'Ponto Registrado! {hora_capturada}'
        notificacao.enviar_notificacao(mensagem)
        time.sleep(60)
'''