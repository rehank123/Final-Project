import streamlit as st

# Define a function to respond to user inputs
def respond_to_message(message):
    if message == "1":
        return "Please select a disease from the list provided."
    elif message == "2":
        return "Please select a disease to find the corresponding doctor."
    elif message == "3":
        return "Please select a doctor to find the corresponding hospital."
    elif message in ["Common Cold", "Influenza (Flu)", "Headache", "Allergies", "Cancer", 
                     "Pneumonia", "Stomach Flu (Gastroenteritis)", "Sinusitis", 
                     "Urinary Tract Infection (UTI)", "Conjunctivitis (Pink Eye)"]:
        return "Recommended medicine: Acetaminophen"  # You can modify these responses as needed
    elif message in ["Dr. Saleem", "Dr. Abdullah", "Dr. Salman", "Dr. Kaleem", "Dr. Naimat", 
                     "Dr. Imran", "Dr. Kamran", "Dr. Moin", "Dr. Sultan", "Dr. Faizan"]:
        return "Hospital Name: Zia Care Hospital"  # You can modify these responses as needed
    else:
        return "Invalid input. Please try again."

# Main Streamlit app code
st.title("Healthcare Chatbot")
st.write("Enter your message below:")

conversation_history = st.text_area("Conversation History", value="", height=400, max_chars=None, key=None)

if conversation_history:
    # Split conversation history into individual messages
    messages = conversation_history.split('\n')
    latest_message = messages[-1]

    # Respond to the latest message
    bot_response = respond_to_message(latest_message)

    # Append bot response to conversation history
    conversation_history += f"\nBot: {bot_response}"

    # Display updated conversation history
    st.text_area("Conversation History", value=conversation_history, height=400, max_chars=None, key=None)

# st.text_input("Please Enter a Number for detail you want to know about:")
