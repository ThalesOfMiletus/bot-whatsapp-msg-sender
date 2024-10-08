# WhatsApp Message Automation

Este projeto é um script em Python que automatiza o envio de mensagens para um grupo específico no WhatsApp.

## Requisitos

- Python 3.6 ou superior
- Instale as bibliotecas necessárias:
  - [pywhatkit](https://pypi.org/project/pywhatkit/): `pip install pywhatkit`
  - [schedule](https://pypi.org/project/schedule/): `pip install schedule`

## Codificação

```python
import pywhatkit as kit
import schedule
import time

# Defina o nome do grupo exatamente como está no WhatsApp
nome_do_grupo = "<nome do grupo que a mensagem será enviada>"

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
