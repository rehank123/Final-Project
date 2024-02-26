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

tabs = ["Chatbot", "Take Appointment", "Appointment Data", "Hospital Addresses", "Upload Tests", "Tests Saved Data", "Contact", "About Us"]
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



import streamlit as st

def hospital_addresses_page():
    st.title("Hospital Addresses")
    st.write("Content for the Hospital Addresses tab goes here.")

    # Dictionary of hospital names, addresses, and image URLs
    hospital_data = {
        "Zia Care Hospital": {
            "address": "Five Star Chorangi",
            "image_url": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1312706413%2Fphoto%2Fmodern-hospital-building.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DoUILskmtaPiA711DP53DFhOUvE7pfdNeEK9CfyxlGio%3D&tbnid=ApFWotwvyklDVM&vet=12ahUKEwiTzbSn5MiEAxVbqycCHXw_DkUQMygBegQIARA1..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fhospital-building&docid=K8s9OO14ksVoTM&w=612&h=444&q=Hospital%20building%20pictures%20330by%20430%20pix&ved=2ahUKEwiTzbSn5MiEAxVbqycCHXw_DkUQMygBegQIARA1"
        },
        "Noor Health Center": {
            "address": "456 Elm Street, City, Country",
            "https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fmodern-style-hospital-building-straight-lines-concrete-facing-30588884.jpg&tbnid=4gIjCfyup5SbMM&vet=12ahUKEwiTzbSn5MiEAxVbqycCHXw_DkUQMygDegQIARA7..i&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Fphotos-images%2Fbuilding-hospital.html&docid=mmg0orFBwNjeUM&w=800&h=704&q=Hospital%20building%20pictures%20330by%20430%20pix&ved=2ahUKEwiTzbSn5MiEAxVbqycCHXw_DkUQMygDegQIARA7"
        },
        "Al-Muslim Medical Center": {
            "address": "789 Oak Street, City, Country",
            "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dhospital%2Bbuilding&psig=AOvVaw037ZT5564Wka8HO0pdmvsH&ust=1709029273667000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCICTvKjkyIQDFQAAAAAdAAAAABAE"
        },
        "Sultan Hospital": {
            "address": "456 Pine Street, City, Country",
            "image_url": "https://example.com/sultan_hospital.jpg"
        },
        "Shaukat Khanum": {
            "address": "789 Maple Street, City, Country",
            "image_url": "https://example.com/shaukat_khanum.jpg"
        },
        "Imam Clinic Hospital": {
            "address": "123 Cedar Street, City, Country",
            "image_url": "https://example.com/imam_clinic_hospital.jpg"
        },
        "Muslim Welfare Hospital": {
            "address": "456 Birch Street, City, Country",
            "image_url": "https://example.com/muslim_welfare_hospital.jpg"
        },
        "Safa Medical Center": {
            "address": "789 Walnut Street, City, Country",
            "image_url": "https://example.com/safa_medical_center.jpg"
        },
        "Al Khidmat Hospital": {
            "address": "123 Oak Street, City, Country",
            "image_url": "https://example.com/al_khidmat_hospital.jpg"
        }
    }

    # Display each hospital name, address, and provide a link for the image URL
    for i, (hospital_name, data) in enumerate(hospital_data.items(), start=1):
        st.write(f"{i}. Hospital Name: {hospital_name}")
        st.write(f"   Address: {data['address']}")
        # Provide a link for the image URL
        st.write(f"   Image URL: [{data['image_url']}]({data['image_url']})")

if __name__ == "__main__":
    hospital_addresses_page()


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
<p>Developed with ❤️ by the student of  <a style='display: block; text-align: Center;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""

# Display the footer content
st.markdown(footer, unsafe_allow_html=True)
