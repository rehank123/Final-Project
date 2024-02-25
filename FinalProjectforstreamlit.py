import streamlit as st

# Define the tabs
tabs = ["Chatbot", "About", "Contact"]
selected_tab = st.sidebar.selectbox("Select a tab", tabs)

# Display content based on the selected tab
if selected_tab == "Chatbot":
    st.title("Welcome to Healthcare Chatbot")
    st.write("Information List")
    st.write("""
    1. About Medicine for Disease
    2. About Doctor for Disease
    3. About Hospital for Doctor
    """)

    # Handle user input for different information options
    information = st.text_input("Please Enter a Number for detail you want to know about:")
    if information == "1":
        st.write("List of diseases")
        st.write("""
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
        """)
        # Add logic to display recommended medicines based on disease input

    elif information == "2":
        st.write("List of Diseases")
        # Add logic to display list of doctors based on disease input

    elif information == "3":
        st.write("List of Doctors")
        # Add logic to display hospital names based on doctor input

    else:
        st.write("Invalid Input")

elif selected_tab == "Contact":
    st.title("Contact")
    st.write("banoqabil.")

elif selected_tab == "About":
    st.title("About")
    # Display information about the chatbot
    st.write("""
    This is a healthcare chatbot designed to provide information about various medical conditions, recommended medicines, doctors, and hospitals.
    You can use the tabs to navigate between different sections:
    - **Home**: Provides options to explore information about medicines, doctors, and hospitals.
    - **About**: Gives a brief overview of the chatbot.
    - **Contact**: Provides contact information.
    """)

# HTML footer
footer = """
<style>
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
<p>Developed with ❤ by the student of => <a style='display: block; text-align: center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""
# Display HTML footer
st.markdown(footer, unsafe_allow_html=True)
