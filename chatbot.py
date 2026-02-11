import openai
import os  # 👈 precisa importar

chave_key = os.getenv("OPENAI_API_KEY")  # 👈 aqui está o segredo

openai.api_key = chave_key

def enviar_mensagem(mensagem, Lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )

    return resposta["choices"][0]["message"]


lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot:", resposta["content"])

print(enviar_mensagem("Em que ano Einstein publicou a teoria geral da relatividade?"))
