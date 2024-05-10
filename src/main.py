import google.generativeai as ai

# Configure credentials
API_KEY = 'YOUR API KEY'
ai.configure(API_KEY)

# Settings for the chatbot generation
generation_config = {
	'candidate': 1, # Number of candidates to generate
	'max_tokens': 100, # Maximum number of tokens to generate
	'temperature': 0.5, # Temperature for sampling
}

# Safety settings to filter out inappropriate content
safety_settings = {
	'HARASSMENT': 'BLOCK_NONE',
	'HATE': 'BLOCK_NONE',
	'SEXUAL': 'BLOCK_NONE',
	'DANGEROUS': 'BLOCK_NONE',
}

# Context for the chatbot
context = """
Este assistente virtual está projetado especificamente para oferecer suporte e informações vitais para indivíduos afetados pelas recentes enchentes no Rio Grande do Sul. Através deste serviço, você pode receber orientações sobre como se preparar para situações de emergência, o que fazer durante uma enchente para manter sua segurança, e como gerenciar a recuperação após o evento. Este assistente está equipado para ajudar com informações atualizadas sobre as condições locais, localização de abrigos temporários, acesso a recursos como bancos de alimentos e apoio emocional. Nosso objetivo é fornecer uma ferramenta acessível e útil para ajudar você a navegar por este período desafiador com informação e suporte confiáveis.
"""

# Initialize the chatbot with model, context and GenAI client
model = ai.GenerativeModel(model_name='gemini-1.0-pro',
							generation_config=generation_config,
							safety_settings=safety_settings,
							context=context,
							)

genai_client = ai.Client(api_key=API_KEY)

# Start the chatbot
chat = model.start_chat(history=[])

print("Olá! Lamento muito pelo que você está passando devido às enchentes no Rio Grande do Sul. Estou aqui para ajudar no que eu puder. Você precisa de abrigo, alimentação, informações ou outro tipo de auxílio?\n")

while True:
    user_input = input("O que você precisa? (abrigo, alimentação, etc. ou digite 'ajuda' para opções):\n").lower()
    if user_input == "end":
        break

    # Generate a response from GenAI based on the user's input, including the context
    response = genai_client.generate(
        prompt=context + "\n\nUsuário: " + user_input + "\nAssistente:",
        max_tokens=150
    )

    print("Assistente: ", response.text, '\n')

    continue_prompt = input("Posso ajudar com mais alguma coisa? (sim/não)\n").lower()
    if continue_prompt != "sim":
        break
