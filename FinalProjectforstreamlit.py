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



st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://banoqabil.pk/media/logo.png" width="200">
    </div>
""", unsafe_allow_html=True)



# Define the tabs
tabs = ["Chatbot", "Take Appointment", "Appointment Data", "Hospitals Preview", "Upload Tests", "Tests Saved Data", "Contact Us", "About Us"]

# Add the "Home" title above the tabs
st.sidebar.markdown("<h1 style='text-align: left; color: red; font-family: Arial, sans-serif; margin-bottom: -200px;'>Go to</h1>", unsafe_allow_html=True)

# Display the radio button for selecting tabs
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

elif selected_tab == "Contact Us":
    st.title("Contact Us")

    st.write("""
    ## Get in Touch

    We're here to assist you with any questions, feedback, or inquiries you may have. Feel free to reach out to us using the contact information provided below:

    ### Contact Information:
    - **Email:** [contact@healthcarechatbot.com](mailto:contact@healthcarechatbot.com)
    - **Phone:** +1 (123) 456-7890
    - **Address:** 123 Healthcare Street, Cityville, State, Country

    ### Social Media:
    Connect with us on social media for the latest updates, news, and announcements:
    - [Twitter](https://twitter.com/healthcarechatbot)
    - [Facebook](https://www.facebook.com/healthcarechatbot)
    - [LinkedIn](https://www.linkedin.com/company/healthcarechatbot)

    ### Support Hours:
    Our dedicated support team is available to assist you during the following hours:
    - Monday to Friday: 9:00 AM - 6:00 PM (Local Time)
    - Saturday: 10:00 AM - 4:00 PM (Local Time)
    - Sunday: Closed

    ### Feedback:
    We value your feedback and suggestions. Please take a moment to complete our [feedback form](https://forms.example.com/feedback) to help us improve our services.

    ### Technical Support:
    For technical assistance or issues related to the healthcare chatbot platform, please email our technical support team at [support@healthcarechatbot.com](mailto:support@healthcarechatbot.com).

    ### Business Partnerships:
    Interested in partnering with us? For business inquiries, collaborations, or partnerships, please contact our business development team at [partnerships@healthcarechatbot.com](mailto:partnerships@healthcarechatbot.com).

    We look forward to hearing from you and assisting you with your healthcare needs!

    **Healthcare Chatbot Team**
    """)


elif selected_tab == "About Us":
    st.title("About Us")

    st.write("""
    ## About Healthcare Chatbot

    **Mission:** Our mission is to provide accessible and reliable healthcare information through innovative technology solutions.

    **Vision:** To empower individuals to make informed decisions about their health and well-being.

    **Values:**
    - **Integrity:** We uphold the highest standards of integrity and ethical conduct in all our interactions.
    - **Excellence:** We strive for excellence in everything we do, delivering quality services and solutions to our users.
    - **Innovation:** We embrace innovation and continuously explore new technologies to enhance the user experience.
    - **Collaboration:** We foster collaboration and partnerships to achieve shared goals and objectives.
    - **Empathy:** We demonstrate empathy and understanding in our interactions with users, recognizing their unique needs and challenges.

    **Key Features:**
    - **Medicine Information:** Access detailed information about medicines and their uses for various health conditions.
    - **Doctor Directory:** Find healthcare professionals based on specialty, location, and availability.
    - **Hospital Locator:** Discover nearby hospitals, clinics, and healthcare facilities with ease.

    **Future Enhancements:**
    - Integration with telemedicine platforms for virtual consultations.
    - Implementation of advanced AI algorithms for personalized healthcare recommendations.
    - Expansion of services to include mental health support and wellness programs.

    **Contact Us:** Have questions or feedback? Get in touch with our team through the [Contact Us](#contact-us) tab.

    Thank you for choosing Healthcare Chatbot for your healthcare needs!
    """)



else:
    st.write("This section is under construction. Check back soon!")

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
