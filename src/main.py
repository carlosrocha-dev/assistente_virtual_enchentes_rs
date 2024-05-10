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