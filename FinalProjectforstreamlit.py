import streamlit as st

def home():
    st.write("# Welcome to Healthcare Chatbot")
    st.write("### Information List")
    st.write("""
    1. About Medicine for Disease
    2. About Doctor for Disease
    3. About Hospital for Doctor
    """)

def medicine_for_disease():
    st.write("## About Medicine for Disease")
    st.write("### List of Diseases")
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

    disease = st.selectbox("Select a disease:", [
        "Common Cold", "Influenza (Flu)", "Headache", "Allergies",
        "Cancer", "Pneumonia", "Stomach Flu (Gastroenteritis)",
        "Sinusitis", "Urinary Tract Infection (UTI)", "Conjunctivitis (Pink Eye)"
    ])

    if disease == "Common Cold":
        st.write("Recommended medicine: Acetaminophen")
    elif disease == "Influenza (Flu)":
        st.write("Recommended medicine: Ibuprofen")
    # Add more options for other diseases

def doctor_for_disease():
    st.write("## About Doctor for Disease")
    st.write("### List of Doctors")
    st.write("""
    1. Cardiologist
    2. Dermatologist
    3. Gastroenterologist
    4. Neurologist
    5. Ophthalmologist
    6. Pediatrician
    7. Psychiatrist
    8. Urologist
    9. Psychologist
    10. Otorhinolaryngologist
    """)

    doctor = st.selectbox("Select a doctor:", [
        "Cardiologist", "Dermatologist", "Gastroenterologist", "Neurologist",
        "Ophthalmologist", "Pediatrician", "Psychiatrist", "Urologist",
        "Psychologist", "Otorhinolaryngologist"
    ])

    if doctor == "Cardiologist":
        st.write("Dr. Saleem")
    elif doctor == "Dermatologist":
        st.write("Dr. Abdullah")
    # Add more options for other doctors

def hospital_for_doctor():
    st.write("## About Hospital for Doctor")
    st.write("### List of Hospitals")
    st.write("""
    1. Muslim Care Hospital
    2. Islamic Health Center
    3. Al-Muslim Medical Center
    4. Nur Muslim Hospital
    5. Muslim Community Hospital
    6. Iman Muslim Hospital
    7. Muslim Welfare Hospital
    8. Safa Muslim Medical Center
    9. Muslim Relief Hospital
    10. Ummu Hospital
    """)

    hospital = st.selectbox("Select a hospital:", [
        "Muslim Care Hospital", "Islamic Health Center", "Al-Muslim Medical Center",
        "Nur Muslim Hospital", "Muslim Community Hospital", "Iman Muslim Hospital",
        "Muslim Welfare Hospital", "Safa Muslim Medical Center", "Muslim Relief Hospital",
        "Ummu Hospital"
    ])

    # You can add more detailed information about each hospital if needed

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "About Medicine", "About Doctor", "About Hospital"])

    if selection == "Home":
        home()
    elif selection == "About Medicine":
        medicine_for_disease()
    elif selection == "About Doctor":
        doctor_for_disease()
    elif selection == "About Hospital":
        hospital_for_doctor()

if __name__ == "__main__":
    main()
