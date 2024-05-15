import telebot
import time
import dotenv
import os
import datetime
import random

dotenv.load_dotenv()
TOKEN = os.getenv("KEY")

# Token do seu bot
bot = telebot.TeleBot(TOKEN)

# Listas de horários de entrada e saída
horarios_entrada = ["7:53", "8:04", "8:12"]
horarios_saida = ["17:05", "17:10", "17:15"]

def enviar_mensagem_automatica(mensagem):
    bot.send_message(7021296280, mensagem)

def verificar_horario():
    # Verificar se é dia útil (segunda a sexta-feira)
    dia_semana = datetime.datetime.today().weekday()
    if dia_semana >= 0 and dia_semana <= 4:  # 0 é segunda-feira, 4 é sexta-feira
        return True
    else:
        return False

def escolher_horarios():
    horario_entrada = random.choice(horarios_entrada)
    horario_saida = random.choice(horarios_saida)
    return horario_entrada, horario_saida

while True:
    if verificar_horario():
        horario_entrada, horario_saida = escolher_horarios()
        mensagem = f"Horário de entrada: {horario_entrada}\nHorário de saída: {horario_saida}"
        enviar_mensagem_automatica(mensagem)
    time.sleep(10)  # Aguarde 10 segundos
