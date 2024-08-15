import pywhatkit as kit
import schedule
import time

# Defina o nome do grupo exatamente como tá no WhatsApp
nome_do_grupo = "Jovem e Tecnologia - Escola Afonso Pena - Paraíso do Sul"

# Mensagem para enviar
mensagem = "Olá, esta é uma mensagem automatizada!"

# Função para enviar a mensagem
def enviar_mensagem():
    kit.sendwhatmsg_to_group(nome_do_grupo, mensagem, 10, 0)  # 10:00 AM

# Agendar a mensagem para segunda e sexta-feira às 10:00
schedule.every().monday.at("10:00").do(enviar_mensagem)
schedule.every().friday.at("10:00").do(enviar_mensagem)

# Loop para manter a automação rodando
while True:
    schedule.run_pending()
    time.sleep(1)
