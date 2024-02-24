import streamlit as st

# Function to provide healthcare advice based on user input
def healthcare_advice(query):
    if "headache" in query.lower():
        return "You can try taking ibuprofen and getting some rest."
    elif "fever" in query.lower():
        return "You should take acetaminophen and consult a doctor if the fever persists."
    elif "cough" in query.lower():
        return "You should avoid exposure to irritants and consider taking cough syrup."
    else:
        return "I am sorry, I do not have information on that."

# Streamlit app title and description
st.title("Healthcare Chat Bot")
st.write("Welcome! Ask me any health-related questions.")

# User input for healthcare query
query = st.text_input("Ask me anything:")

# Button to submit query
if st.button("Get Advice"):
    # Get healthcare advice based on user query
    advice = healthcare_advice(query)
    # Display healthcare advice
    st.write("HealthcareBot:", advice)
