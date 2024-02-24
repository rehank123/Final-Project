from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot
chatbot = ChatBot('HealthcareBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Define some custom rules for healthcare-related queries
healthcare_rules = {
    'cold': 'You should rest and drink plenty of fluids.',
    'fever': 'You should take acetaminophen and consult a doctor if the fever persists.',
    'headache': 'You can try taking ibuprofen and getting some rest.',
    'cough': 'You should avoid exposure to irritants and consider taking cough syrup.'
}

# Function to process user queries and provide responses
def healthcare_chat(query):
    response = healthcare_rules.get(query.lower(), 'I am sorry, I do not have information on that.')
    return response

# Main loop to interact with the chatbot
print("Welcome to Healthcare Chat Bot!")
print("You can ask questions related to common health issues.")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Exiting the chat. Goodbye!")
        break
    else:
        response = healthcare_chat(user_input)
        print("HealthcareBot:", response)
