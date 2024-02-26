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

tabs = ["Chatbot", "Take Appointment", "Appointment Data", "Hospitals Preview", "Upload Tests", "Tests Saved Data", "Contact", "About Us"]
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

elif selected_tab == "Appointment Data":
    st.title("Appointment Data")

    # Load existing appointment data from CSV
    try:
        existing_data = pd.read_csv("appointments.csv")
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=["Patient Name", "Doctor", "Disease", "Date", "Time", "Reason"])

    # Filter appointments by selected doctor
    st.sidebar.title("Filter by Doctor")
    selected_doctor = st.sidebar.selectbox("Select Doctor", ["All"] + list(existing_data["Doctor"].unique()))

    if selected_doctor != "All":
        existing_data = existing_data[existing_data["Doctor"] == selected_doctor]

    # Display data table in the main column
    st.write("Below is the list of all saved appointments:")
    if not existing_data.empty:
        st.dataframe(existing_data)

        # Allow users to input the index or indices of rows to delete
        rows_to_delete_input = st.text_input("Enter index or indices of rows to delete (comma-separated):")

        if st.button("Delete rows"):
            try:
                # Convert input string to a list of integers
                indices_to_delete = [int(index.strip()) for index in rows_to_delete_input.split(",")]

                # Remove the specified rows from the DataFrame
                existing_data.drop(indices_to_delete, inplace=True)

                # Save the updated DataFrame back to the CSV file
                existing_data.to_csv("appointments.csv", index=False)

                st.success("Selected rows deleted successfully!")
            except Exception as e:
                st.error(f"An error occurred while deleting rows: {e}")

        # Count the number of appointments per doctor
        appointment_counts = existing_data['Doctor'].value_counts()

        # Plotting the bar chart in the sidebar
        st.sidebar.title('Number of Appointments per Doctor')
        st.sidebar.bar_chart(appointment_counts)

    else:
        st.write("No appointments found.")

elif selected_tab == "Hospitals Preview":
    st.title("Hospitals Preview")
    st.write("Picture of Zia Hospital.")

    # URL of the hospital building image
    image_url = "https://media.istockphoto.com/id/1312706413/photo/modern-hospital-building.jpg?s=612x612&w=0&k=20&c=oUILskmtaPiA711DP53DFhOUvE7pfdNeEK9CfyxlGio%3D"
    # Display the hospital building image
    st.image(image_url, caption="Hospital Building", use_column_width=True)
    
    st.title("Hospitals Preview")
    st.write("Picture of Zia Hospital.")
   image_url = "data:image/jpeg;base64,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"

    # Display the hospital building image
    st.image(image_url, caption="Hospital Building", use_column_width=True)
    

elif selected_tab == "Upload Tests":
    st.title("Upload Tests")
    st.write("Please fill out the form and upload the test picture.")

    # Create a form for test picture upload
    test_name = st.text_input("Test Name")
    patient_name = st.text_input("Patient Name")
    test_date = st.date_input("Test Date")
    test_result = st.selectbox("Test Result", ["Positive", "Negative"])

    uploaded_file = st.file_uploader("Upload Test Picture", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded file to the upload directory
        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Test picture uploaded successfully!")

        # Save test data
        try:
            # Load existing test data from CSV
            try:
                existing_data = pd.read_csv("tests_saved_data.csv")
            except FileNotFoundError:
                existing_data = pd.DataFrame(columns=["Test Name", "Patient Name", "Test Date", "Test Result", "File Path"])

            # Append the new test data
            new_test = pd.DataFrame({"Test Name": [test_name], "Patient Name": [patient_name], "Test Date": [test_date], "Test Result": [test_result], "File Path": [file_path]})
            existing_data = pd.concat([existing_data, new_test], ignore_index=True)

            # Save the updated DataFrame back to the CSV file
            existing_data.to_csv("tests_saved_data.csv", index=False)

            st.success("Test data saved successfully!")
        except Exception as e:
            st.error(f"An error occurred while saving test data: {e}")
    else:
        st.warning("Please upload a test picture.")

elif selected_tab == "Tests Saved Data":
    st.title("Tests Saved Data")

    # Load and display saved test data
    try:
        tests_data = pd.read_csv("tests_saved_data.csv")
        if not tests_data.empty:
            st.dataframe(tests_data)

            # Allow users to input the index or indices of rows to delete
            rows_to_delete_input = st.text_input("Enter index or indices of rows to delete (comma-separated):")

            if st.button("Delete rows"):
                try:
                    # Convert input string to a list of integers
                    indices_to_delete = [int(index.strip()) for index in rows_to_delete_input.split(",")]

                    # Remove the specified rows from the DataFrame
                    tests_data.drop(indices_to_delete, inplace=True)

                    # Save the updated DataFrame back to the CSV file
                    tests_data.to_csv("tests_saved_data.csv", index=False)

                    st.success("Selected rows deleted successfully!")
                except Exception as e:
                    st.error(f"An error occurred while deleting rows: {e}")
        else:
            st.write("No tests saved yet.")
    except FileNotFoundError:
        st.write("No tests saved yet.")

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
    - *Home*: Provides options to explore information about medicines, doctors, and hospitals.
    - *About Us*: Gives a brief overview of the chatbot.
    - *Contact*: Provides contact information.
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
<p>Developed with ❤️ by the student of  <a style='display: block; text-align: Center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""

# Display the footer content
st.markdown(footer, unsafe_allow_html=True)
