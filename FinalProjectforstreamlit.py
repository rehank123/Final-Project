import streamlit as st
import openai

st.title("Healthcare Chatbot")

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

user_input = st.text_input("Please Enter a Number for detail you want to know about:")

if user_input:
    st.session_state.messages = [{"role": "user", "content": user_input}]
    full_response = ""
    for response in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]}
                  for m in st.session_state.messages], stream=True):
        full_response += response.choices[0].delta.get("content", "")
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    if user_input == "1":
        st.write("User: ", user_input)
        st.write("Chatbot: Please select a disease from the list provided.")
    elif user_input == "2":
        st.write("User: ", user_input)
        st.write("Chatbot: Please select a disease to find the corresponding doctor.")
    elif user_input == "3":
        st.write("User: ", user_input)
        st.write("Chatbot: Please select a doctor to find the corresponding hospital.")
    else:
        st.write("User: ", user_input)
        st.write("Chatbot: Invalid Input")

    st.write("Chatbot: ", full_response)
