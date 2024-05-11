import os
import google.generativeai as ai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = os.getenv('GOOGLE_API_KEY')
ai.configure(api_key=API_KEY)
context = "Este assistente virtual está projetado especificamente para oferecer suporte e informações vitais para indivíduos afetados pelas recentes enchentes no Rio Grande do Sul le outros desastres naturais que tornam as pessoas vulneraveis e com risco de morte. Através deste serviço, você pode receber orientações sobre como se preparar para situações de emergência, o que fazer durante uma enchente para manter sua segurança, e como gerenciar a recuperação após o evento. Este assistente está equipado para ajudar com informações atualizadas sobre as condições locais, localização de abrigos temporários, acesso a recursos como bancos de alimentos e apoio emocional. Nosso objetivo é fornecer uma ferramenta acessível e útil para ajudar você a navegar por este período desafiador com informação e suporte confiáveis."
model = ai.GenerativeModel(model_name='gemini-1.0-pro',
							generation_config={'temperature': 0.5},
							safety_settings={
											'HARASSMENT': 'BLOCK_NONE',
											'HATE': 'BLOCK_NONE',
											'SEXUAL': 'BLOCK_NONE',
											'DANGEROUS': 'BLOCK_NONE'
											})
chat = model.start_chat(history=[])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
	userText = request.form['msg']
	response = chat.send_message(context + userText)
	return jsonify(message=response.text)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
