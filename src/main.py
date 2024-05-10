import google.generativeai as ai

# Configure credentials
API_KEY = 'AIzaSyBQYNykGhYNcvzjKatX7MBgmE6wS1kw-Og'
ai.configure(api_key=API_KEY)

# Settings for the chatbot generation
generation_config = {
    'temperature': 0.5,  # Temperature for sampling
}

# Safety settings to filter out inappropriate contents
safety_settings = {
    'HARASSMENT': 'BLOCK_NONE',
    'HATE': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE',
}

# Context for the chatbot
context = "Este assistente virtual está projetado especificamente para oferecer suporte e informações vitais para indivíduos afetados pelas recentes enchentes no Rio Grande do Sul le outros desastres naturais que tornam as pessoas vulneraveis e com risco de morte. Através deste serviço, você pode receber orientações sobre como se preparar para situações de emergência, o que fazer durante uma enchente para manter sua segurança, e como gerenciar a recuperação após o evento. Este assistente está equipado para ajudar com informações atualizadas sobre as condições locais, localização de abrigos temporários, acesso a recursos como bancos de alimentos e apoio emocional. Nosso objetivo é fornecer uma ferramenta acessível e útil para ajudar você a navegar por este período desafiador com informação e suporte confiáveis."

# Initialize the chatbot with model, context and GenAI client
model = ai.GenerativeModel(model_name='gemini-1.0-pro',
                           generation_config=generation_config,
                           safety_settings=safety_settings)

# Start the chatbot
chat = model.start_chat(history=[])

prompt = input("\n\033[1;32mComo posso ajudá-lo(a) hoje? Estou aqui para oferecer suporte. Por favor, conte-me o que você precisa.\033[0m\n\n")

while prompt != "sair":
	response = chat.send_message(context + prompt)
	print("\033[1;32mAssistente: \033[0m\n", response.text, '\n')
	prompt = input("\033[1;32mPosso ajudar com mais alguma coisa? \n(Para encerrar essa conversa digite `sair`)\033[0m\n")

if prompt == "sair":
	print("\033[1;32mObrigado por usar o assistente virtual. Fique seguro e cuide-se!\033[0m\n")
