from openai import OpenAI
# from dotenv import load_dotenv        # No se requiere dotenv

SYSTEM_MESSAGE = "You are a chatbot. You will have a conversation with a user. Be friendly and concise"

if __name__ == "__main__":
    URL = "http://127.0.0.1:1234/v1"    # El enlace del servidor local de LM Studio
    KEY = "."                           # La llave API NO se requiere por LM Studio (se ignora) 
    MODEL = "google/gemma-4-e4b"        # El nombre completo del modelo LLM local para que se seleccione.

    client = OpenAI(
        base_url=URL,
        api_key=KEY,
    )

    print(f"Chatting with {MODEL} model at LM Studio ({URL})\n")

    while True:
        message = input("> ")
        
        # Se utliza un simbolo slash (/) para activar el comando
        if message[0] == "/":
            if message.lower() == "/end": # Cerrar este programa
                break
        elif message[0] != "/":
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {'role': 'system', 'content': SYSTEM_MESSAGE},
                    {'role': 'user', 'content': message},
                ]
            )
            print(response.choices[0].message.content)
