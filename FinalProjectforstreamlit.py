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

if "messages" not in st.session_state:
    st.session_state.messages = []

diseases_list = """
1. Common Cold
2. Influenza (Flu)
3. Headache
4. Allergies
5. Cancer
6. Pneumonia
7. Stomach Flu (Gastroenteritis)
8. Sinusitis
9. Urinary Tract Infection (UTI)
10. Conjunctivitis (Pink Eye)
"""

doctors_list = """
1. Dr. Saleem
2. Dr. Abdullah
3. Dr. Salman
4. Dr. Kaleem
5. Dr. Naimat
6. Dr. Imran
7. Dr. Kamran
8. Dr. Moin
9. Dr. Sultan
10. Dr. Faizan
"""

hospitals_list = """
1. Zia Care Hospital
2. Noor Health Center
3. Al-Muslim Medical Center
4. Sultan Hospital
5. Shaukat Khanum
6. Imam Clinic Hospital
7. Muslim Welfare Hospital
8. Safa Medical Center
9. Al Khidmat Hospital
10. Zain Hospital
"""

information_list = """
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
"""

user_input = st.selectbox("Please select an option:", information_list.split("\n"))

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
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
        st.write("Diseases List: ")
        st.write(diseases_list)
    elif user_input == "2":
        st.write("User: ", user_input)
        st.write("Chatbot: Please select a disease to find the corresponding doctor.")
        st.write("Doctors List: ")
        st.write(doctors_list)
    elif user_input == "3":
        st.write("User: ", user_input)
        st.write("Chatbot: Please select a doctor to find the corresponding hospital.")
        st.write("Hospitals List: ")
        st.write(hospitals_list)
    else:
        st.write("User: ", user_input)
        st.write("Chatbot: Invalid Input")

    st.write("Chatbot: ", full_response)
