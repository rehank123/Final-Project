import streamlit as st

st.header('This is a header with a divider', divider='rainbow')
st.header('_ Muhammad Amaan_ is :blue[cool] :sunglasses:')
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)import streamlit as st

def health_chatbot():
    st.title("Health Chatbot")

    st.sidebar.title("User Input")
    user_input = st.sidebar.text_area("Enter your message")

    if st.sidebar.button("Ask"):
        bot_response = get_bot_response(user_input)
        st.write("Bot:", bot_response)

def get_bot_response(user_input):
    # Simple rule-based responses
    if "symptoms" in user_input.lower():
        return "Please consult a doctor for accurate diagnosis and treatment."
    elif "fever" in user_input.lower():
        return "Fever could be a sign of an underlying condition. Make sure to stay hydrated and rest. If it persists, consult a doctor."
    elif "headache" in user_input.lower():
        return "Headaches can be due to various reasons. Ensure you're well-hydrated and consider taking a break if you've been staring at screens for too long."
    else:
        return "I'm sorry, I couldn't understand that. Please provide more information or rephrase your question."

if __name__ == "__main__":
    health_chatbot()
