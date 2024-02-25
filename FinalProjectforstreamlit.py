import streamlit as st

# Set the background color to gray
st.set_page_config(layout="wide", page_title="Healthcare Chatbot", page_icon=":hospital:",
                   initial_sidebar_state="collapsed", theme="gray")

st.title("Welcome to Healthcare Chatbot")
st.write("Information List")
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
""")

information = st.selectbox("Please select the information you want to know about:",
                            ["About Medicine for Disease", "About Doctor for Disease", "About Hospital for Doctor"])

if information == "About Medicine for Disease":
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

    disease = st.selectbox("Select your disease for Medicine:",
                           ["Common Cold", "Influenza (Flu)", "Headache", "Allergies", "Cancer",
                            "Pneumonia", "Stomach Flu (Gastroenteritis)", "Sinusitis", "UTI", "Conjunctivitis (Pink Eye)"])

    # Define a dictionary to map diseases to recommended medicines
    medicine_recommendations = {
        "Common Cold": "Acetaminophen",
        "Influenza (Flu)": "Ibuprofen",
        "Headache": "Aspirin",
        "Allergies": "Loratadine",
        "Cancer": "Paclitaxel (Consult a doctor immediately)",  # Emphasize seeking professional help
        "Pneumonia": "Amoxicillin (Consult a doctor immediately)",
        "Stomach Flu (Gastroenteritis)": "Loperamide",
        "Sinusitis": "Decongestants",
        "UTI": "Phenazopyridine (Consult a doctor immediately)",
        "Conjunctivitis (Pink Eye)": "Artificial tears"
    }

    if disease in medicine_recommendations:
        st.write(f"Recommended medicine: {medicine_recommendations[disease]}")
    else:
        st.write("Your disease is not in the list. Please consult a doctor for proper diagnosis and treatment.")

elif information == "About Doctor for Disease":
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

    doctor = st.selectbox("Select your disease for Doctor:",
                           ["Common Cold", "Influenza (Flu)", "Headache", "Allergies", "Cancer",
                            "Pneumonia", "Stomach Flu (Gastroenteritis)", "Sinusitis", "UTI", "Conjunctivitis (Pink Eye)"])

    # Define a dictionary to map diseases to doctors
    doctor_associations = {
        "Common Cold": "Dr. Saleem",
        "Influenza (Flu)": "Dr. Abdullah",
        "Headache": "Dr. Salman",
        "Allergies": "Dr. Kaleem",
        "Cancer": "Consult a specialized oncologist immediately",  # Emphasize seeking specialized care
        "Pneumonia": "Consult a pulmonologist immediately",
        "Stomach Flu (Gastroenteritis)": "Dr. Naimat",
        "Sinusitis": "Dr. Imran",
        "UTI": "Dr. Kamran",
        "Conjunctivitis (Pink Eye)": "Dr. Moin"
    }

    if doctor in doctor_associations:
        st.write(f"Doctor for this disease: {doctor_associations[doctor]}")
    else:
        st.write("Consult a doctor for proper diagnosis and treatment.")

elif information == "About Hospital for Doctor":
    st.write("List of Doctors")
    st.write("""
    1. Dr. Saleem
    2. Dr. Abdullah
    3. Dr. Salman
    4. Dr. Kaleem
    5. Consult a specialized oncology hospital
    6. Consult a pulmonology hospital
    7. Dr. Naimat
    8. Dr. Imran
    9. Dr. Kamran
    10. Dr. Moin
    """)

