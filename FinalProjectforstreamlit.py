import streamlit as st
import pandas as pd

tabs = [
    "Chatbot",
    "Take Appointment",
    "Saved Data",
    "Hospital Addresses",
    "Contact",
    "About Us"
]
selected_tab = st.sidebar.radio("", tabs)

if selected_tab == "Chatbot":
    st.title("Welcome to Healthcare Chatbot")
    st.write("Information List")
    st.write("""
    1. About Medicine for Disease
    2. About Doctor for Disease
    3. About Hospital for Doctor
    """)

    information = st.text_input("Please Enter a Number for detail you want to know about:")

    if information == "1":
        st.write("List of diseases")
        st.write("""
        1. Common Cold
        2. Influenza (Flu)
        3. Headache
        ...
        """)
        # Medicine recommendation logic based on disease input

    elif information == "2":
        st.write("List of Diseases")
        st.write("""
        1. Common Cold
        2. Influenza (Flu)
        3. Headache
        ...
        """)
        # Doctor information based on disease input

    elif information == "3":
        st.write("List of Doctors")
        st.write("""
        1. Dr. Saleem
        2. Dr. Abdullah
        3. Dr. Salman
        ...
        """)
        # Hospital information based on doctor input

    else:
        st.write("Invalid Input")

elif selected_tab == "Take Appointment":
    # Appointment scheduling functionality
    st.title("Take Doctor Appointment")
    ...
    
    # Existing appointment data from CSV

elif selected_tab == "Saved Data":
    # Logic for displaying saved data
    ...

elif selected_tab == "Hospital Addresses":
    # Logic for displaying hospital addresses
    ...

elif selected_tab == "Contact":
    # Logic for displaying contact information
    ...

elif selected_tab == "About Us":
    # Logic for displaying About Us section
    ...

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
<p>Developed with ❤️ by the student of <a style='display: block; text-align: Right;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat</a></p>
</div>
"""
