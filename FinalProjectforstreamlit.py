import streamlit as st
import pandas as pd
import os

upload_dir = "uploaded_tests"
os.makedirs(upload_dir, exist_ok=True)

doctor_diseases = {
    "Dr. Saleem": ["Common Cold", "Influenza (Flu)", "Headache"],
    "Dr. Abdullah": ["Allergies", "Cancer", "Pneumonia"],
    "Dr. Salman": ["Stomach Flu (Gastroenteritis)", "Sinusitis", "Urinary Tract Infection (UTI)"],
    "Dr. Kaleem": ["Conjunctivitis (Pink Eye)"],
    "Dr. Naimat": ["Common Cold", "Headache", "Allergies"],
    "Dr. Imran": ["Influenza (Flu)", "Cancer", "Sinusitis"],
    "Dr. Kamran": ["Pneumonia", "Stomach Flu (Gastroenteritis)", "Urinary Tract Infection (UTI)"],
    "Dr. Moin": ["Headache", "Conjunctivitis (Pink Eye)"],
    "Dr. Sultan": ["Common Cold", "Allergies", "Pneumonia"],
    "Dr. Faizan": ["Influenza (Flu)", "Cancer", "Sinusitis"]
}

tabs = ["Chatbot", "Take Appointment", "Appointment Data", "Upload Tests", "Tests Saved Data", "Contact", "About Us"]
selected_tab = st.sidebar.radio("", tabs)

if selected_tab == "Chatbot":
    st.title("Welcome to Healthcare Chatbot 🤖")
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
        4. Allergies
        5. Cancer
        6. Pneumonia
        7. Stomach Flu (Gastroenteritis)
        8. Sinusitis
        9. Urinary Tract Infection (UTI)
        10. Conjunctivitis (Pink Eye)
        """)

        disease = st.text_input("Enter the number of your disease for Medicine:")

        if disease == "1":  
            st.write("Recommended medicine: Acetaminophen")
        elif disease == "2":
            st.write("Recommended medicine: Ibuprofen")
        elif disease == "3":
            st.write("Recommended medicine: Aspirin")
        elif disease == "4":
            st.write("Recommended medicine: Loratadine")
        elif disease == "5":
            st.write("Recommended medicine: Paclitaxel")
        elif disease == "6":
            st.write("Recommended medicine: Amoxicillin")
        elif disease == "7":
            st.write("Recommended medicine: Loperamide")
        elif disease == "8":
            st.write("Recommended medicine: Decongestants")
        elif disease == "9":
            st.write("Recommended medicine: Phenazopyridine")
        elif disease == "10":
            st.write("Recommended medicine: Artificial tears")
        else:
            st.write("Your disease is not in the list")

    elif information == "2":
        st.write("List of Diseases")
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
        doctor = st.text_input("Enter the number of your Doctor for Diseases:")

        if doctor == "1":
            st.write("Dr. Saleem")
        elif doctor == "2":
            st.write("Dr. Abdullah")
        elif doctor == "3":
            st.write("Dr. Salman")
        elif doctor == "4":
            st.write("Dr. Kaleem")
        elif doctor == "5":
            st.write("Dr. Naimat")
        elif doctor == "6":
            st.write("Dr. Imran")
        elif doctor == "7":
            st.write("Dr. Kamran")
        elif doctor == "8":
            st.write("Dr. Moin")
        elif doctor == "9":
            st.write("Dr. Sultan")
        elif doctor == "10":
            st.write("Dr. Faizan")
        else:
            st.write("Invalid Input")

    elif information == "3":
        st.write("List of Doctors")
        st.write("""
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
        """)
        doctor = st.text_input("Enter the number of your Doctor for Hospital:")

        if doctor == "1":
            st.write("Hospital Name: Zia Care Hospital")
        elif doctor == "2":
            st.write("Hospital Name: Noor Health Center")
        elif doctor == "3":
            st.write("Hospital Name: Al-Muslim Medical Center")
        elif doctor == "4":
            st.write("Hospital Name: Sultan Hospital")
        elif doctor == "5":
            st.write("Hospital Name: Shaukat Khanum")
        elif doctor == "6":
            st.write("Hospital Name: Imam Clinic Hospital")
        elif doctor == "7":
            st.write("Hospital Name: Muslim Welfare Hospital")
        elif doctor == "8":
            st.write("Hospital Name: Safa  Medical Center")
        elif doctor == "9":
            st.write("Hospital Name: Al Khidmat Hospital")
        elif doctor == "10":
            st.write("Hospital Name: Zain Hospital")
    else:
        st.write("Invalid Input")

elif selected_tab == "Take Appointment":
    st.title("Take Doctor Appointment")
    st.write("Please fill out the form below to schedule a doctor appointment.")

    # Create a form for doctor appointment scheduling
    patient_name = st.text_input("Patient Name")
    doctor = st.selectbox("Select Doctor", ["Dr. Saleem", "Dr. Abdullah", "Dr. Salman", "Dr. Kaleem", "Dr. Naimat", "Dr. Imran", "Dr. Kamran", "Dr. Moin", "Dr. Sultan", "Dr. Faizan"])

    # Populate diseases based on selected doctor
    diseases = doctor_diseases.get(doctor, [])

    # Convert diseases list to dictionary for selectbox options
    disease_options = {disease: disease for disease in diseases}

    disease = st.selectbox("Select Disease", list(disease_options.keys()))

    date = st.date_input("Date")
    time = st.time_input("Time")
    reason = st.text_area("Reason for Appointment")

    if st.button("Schedule Appointment"):
        try:
            # Load existing appointment data from CSV
            try:
                existing_data = pd.read_csv("appointments.csv")
            except FileNotFoundError:
                existing_data = pd.DataFrame(columns=["Patient Name", "Doctor", "Disease", "Date", "Time", "Reason"])

            # Concatenate the new appointment data with the existing DataFrame
            new_appointment = pd.DataFrame({"Patient Name": [patient_name], "Doctor": [doctor], "Disease": [disease], "Date": [date], "Time": [time], "Reason": [reason]})
            existing_data = pd.concat([existing_data, new_appointment], ignore_index=True)

            # Save the updated DataFrame back to the CSV file
            existing_data.to_csv("appointments.csv", index=False)

            st.success("Doctor appointment scheduled successfully!")
            st.write("Patient Name:", patient_name)
            st.write("Doctor:", doctor)
            st.write("Disease:", disease)
            st.write("Date:", date)
            st.write("Time:", time)
            st.write("Reason:", reason)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Add the rest of the tabs in a similar manner

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
<p>Developed with ❤️ by the student of  <a style='display: block; text-align: Center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""

# Display the footer content
st.markdown(footer, unsafe_allow_html=True)
