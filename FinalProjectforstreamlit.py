import streamlit as st

tabs = ["Chatbot", "Take Appointment", "Saved Data", "Hospital Addresses", "Contact", "About Us"]
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
    st.title("Take Appointment")
    st.write("Content for the Take Appointment tab goes here.")

    class Patient:
        def __init__(self, name, age, gender, doctor_specialization):
            self.name = name
            self.age = age
            self.gender = gender
            self.doctor_specialization = doctor_specialization

    patients = []
    total_patients = 0

    doctor_specializations = {
        1: 'Cardiologist',
        2: 'Dermatologist',
        3: 'Pediatrician',
        4: 'Orthopedic',
        5: 'Neurologist'
    }

    def book_appointment():
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        gender = input("Enter patient's gender: ")
        print("Specializations:")
        for key, value in doctor_specializations.items():
            print(f"{key}. {value}")
        choice = int(input("Choose doctor's specialization: "))
        doctor_specialization = doctor_specializations.get(choice)
        if doctor_specialization is None:
            print("Invalid choice.")
            return
        new_patient = Patient(name, age, gender, doctor_specialization)
        patients.append(new_patient)
        global total_patients
        total_patients += 1
        print(f"Appointment booked for {name} with {doctor_specialization}")
        input("Press Enter to continue....")
        print("")

    def view_appointments():
        if total_patients == 0:
            print("No appointments booked yet.")
            return
        print("List of Appointments:")
        for i, patient in enumerate(patients, start=1):
            print(f"{i}. Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Doctor: {patient.doctor_specialization}")
        input("Press Enter to continue....")
        print("")

    while True:
        if total_patients == 0:
            print("No appointments booked yet.")
        else:
            print(f"Total appointments booked: {total_patients}")
        print("")
        print("Enter an option: ")
        print("1. Book an appointment")
        print("2. View appointments")
        print("3. Exit")
        print("")

        option = int(input())

        if option == 1:
            book_appointment()
        elif option == 2:
            view_appointments()
        elif option == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            print("")

elif selected_tab == "Contact":
    st.title("Contact")

    # Custom CSS for styling the contact information box
    contact_styles = """
    <style>
    .contact-box {
        background-color: #f4f4f4; /* Light gray background */
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1); /* Box shadow for depth */
    }
    .contact-info {
        font-size: 18px;
        margin-bottom: 10px;
    }
    .contact-info a {
        color: #0366d6; /* Blue color for links */
        text-decoration: none;
    }
    </style>
    """
    st.markdown(contact_styles, unsafe_allow_html=True)

    # Display the contact information inside a styled box
    st.markdown("### Get in Touch")
    st.markdown("""
    <div class="contact-box">
        <div class="contact-info">
            Phone Number:                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="tel:+923118003480">0311 8003480</a><br>
            WhatsApp Number:                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <a href="https://wa.me/923118003480">0311 8003480</a><br>
            Facebook ID:                  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <a href="https://www.facebook.com/rehan.ullah">Rehan Ullah</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_tab == "About Us":
    st.title("About Us")
    # Display information about the chatbot
    st.write("""
    This is a healthcare chatbot designed to provide information about various medical conditions, recommended medicines, doctors, and hospitals.
    You can use the tabs to navigate between different sections:
    - **Home**: Provides options to explore information about medicines, doctors, and hospitals.
    - **About Us**: Gives a brief overview of the chatbot.
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
<p>Developed with ❤ by the student of  <a style='display: block; text-align: center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""
# Display HTML footer
st.markdown(footer, unsafe_allow_html=True)
