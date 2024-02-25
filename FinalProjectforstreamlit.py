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
    st.title("Take Doctor Appointment")
    st.write("Please fill out the form below to schedule a doctor appointment.")

    # Create a form for doctor appointment scheduling
    patient_name = st.text_input("Patient Name")
    doctor = st.selectbox("Select Doctor", ["Dr. Saleem", "Dr. Abdullah", "Dr. Salman", "Dr. Kaleem", "Dr. Naimat", "Dr. Imran", "Dr. Kamran", "Dr. Moin", "Dr. Sultan", "Dr. Faizan"])
    date = st.date_input("Date")
    time = st.time_input("Time")
    reason = st.text_area("Reason for Appointment")
    submit_button = st.form_submit_button(label='Schedule Appointment')

    if submit_button:
        # Process the form submission (you can save the appointment record to a database, for example)
        st.success("Doctor appointment scheduled successfully!")
        st.write("Patient Name:", patient_name)
        st.write("Doctor:", doctor)
        st.write("Date:", date)
        st.write("Time:", time)
        st.write("Reason:", reason)

elif selected_tab == "Hospital Addresses":
    st.title("Hospital Addresses")
    st.write("Content for the Hospital Addresses tab goes here.")

    # Define the image URLs and captions
    image_urls = [
        "https://www.gettyimages.com/detail/photo/study-of-architectural-form-05-royalty-free-image/173799627",
        "https://stock.adobe.com/images/build-hospital/45207005",
        "https://stock.adobe.com/images/emergeny-room/30021050",
        "https://stock.adobe.com/images/build-hospital/45207005",
        "https://stock.adobe.com/images/build-hospital/45207005",
        "https://stock.adobe.com/images/emergeny-room/30021050"
    ]
    captions = [
        "Zia Hospital North Nazimabad Karachi",
        "Noor Health Care Manghopir Sultanabad Karachi",
        "Al-Muslim Medical Center Malik Chook Lahore",
        "Imam Health Care Five Star Churangi Karachi",
        "Ahmed Ibrahim Eye Hospital Banaras Karachi",
        "Al Khidmat Medical Center Sahiwal "
    ]

    # Create two columns for each image
    col1, col2 = st.columns(2)

    # Display images in each column
    with col1:
        st.image(image_urls[0], caption=captions[0], width=200)
        st.image(image_urls[1], caption=captions[1], width=200)
        st.image(image_urls[2], caption=captions[2], width=200)

    with col2:
        st.image(image_urls[3], caption=captions[3], width=200)
        st.image(image_urls[4], caption=captions[4], width=200)
        st.image(image_urls[5], caption=captions[5], width=200)

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
<p>Developed with ❤️ by the student of  <a style='display: block; text-align: Right;' href="https://banoqabil.pk" target="_blank">Bano Qabil Alkhidmat </a></p>
</div>
"""

# Display the footer content
st.markdown(footer)
