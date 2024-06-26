# main.py

import time
import os
from datetime import datetime
from notificacao_telegram import Notificacao  # Importa a classe Notificacao do arquivo notificacao.py

if __name__ == '__main__':
    while True:
        # Instancia
        notificacao = Notificacao(os.getenv("KEY"))

        # Pega a hora do ponto
        hora_capturada = datetime.now().strftime("%H:%M:%S")
        
        # Envia a mensagem
        mensagem = f'Ponto Registrado! {hora_capturada}'
        notificacao.enviar_notificacao(mensagem)
        time.sleep(60)
