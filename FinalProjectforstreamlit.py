import streamlit as st

# Function to provide recommended medicine based on disease number
def get_recommended_medicine(disease):
    medicines = {
        "1": "Acetaminophen",
        "2": "Ibuprofen",
        "3": "Aspirin",
        "4": "Loratadine",
        "5": "Azithromycin",
        "6": "Amoxicillin",
        "7": "Loperamide",
        "8": "Decongestants",
        "9": "Phenazopyridine",
        "10": "Artificial tears"
    }
    return medicines.get(disease, "Unknown")

# Function to provide doctor's name based on doctor number
def get_doctor_name(doctor):
    doctors = {
        "1": "Dr. Saleem",
        "2": "Dr. Abdullah",
        "3": "Dr. Salman",
        "4": "Dr. Kaleem",
        "5": "Dr. Naimat",
        "6": "Dr. Imran",
        "7": "Dr. Kamran",
        "8": "Dr. Moin",
        "9": "Dr. Sultan",
        "10": "Dr. Faizan"
    }
    return doctors.get(doctor, "Unknown")

# Function to provide hospital name based on doctor number
def get_hospital_name(doctor):
    hospitals = {
        "1": "Muslim Care Hospital",
        "2": "Islamic Health Center",
        "3": "Al-Muslim Medical Center",
        "4": "Nur Muslim Hospital",
        "5": "Muslim Community Hospital",
        "6": "Iman Muslim Hospital",
        "7": "Muslim Welfare Hospital",
        "8": "Safa Muslim Medical Center",
        "9": "Muslim Relief Hospital",
        "10": "Ummu Hospital"
    }
    return hospitals.get(doctor, "Unknown")

# Streamlit app title and description
st.title("Welcome to Healthcare Chat Bot")
st.write("Information List")
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
""")

# User input for information selection
information = st.selectbox("Select the information you want to know about:", ["", "About Medicine for Disease", "About Doctor for Disease", "About Hospital for Doctor"])

# Conditional logic based on user input
if information == "About Medicine for Disease":
    # Display list of diseases
    st.write("List of diseases")
    st.write("""
    1. Common Cold
    2. Influenza (Flu)
    3. Headache
    4. Allergies
    5. Bronchitis
    6. Pneumonia
    7. Stomach Flu (Gastroenteritis)
    8. Sinusitis
    9. Urinary Tract Infection (UTI)
    10. Conjunctivitis (Pink Eye)
    """)

    # User input for disease selection
    disease = st.text_input("Enter the number of your disease:")

    # Display recommended medicine based on disease selection
    recommended_medicine = get_recommended_medicine(disease)
    st.write(f"Recommended medicine: {recommended_medicine}")

elif information == "About Doctor for Disease":
    # Display list of doctors
    st.write("List of Doctors")
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

    # User input for doctor selection
    doctor = st.text_input("Enter the number of your Doctor:")

    # Display doctor's name based on selection
    doctor_name = get_doctor_name(doctor)
    st.write(f"Doctor's Name: {doctor_name}")

elif information == "About Hospital for Doctor":
    # Display list of hospitals
    st.write("List of Hospitals")
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

    # User input for hospital selection based on doctor
    doctor = st.text_input("Enter the number of your Doctor:")
    
    # Display hospital name based on doctor selection
    hospital_name = get_hospital_name(doctor)
    st.write(f"Hospital Name: {hospital_name}")

else:
    st.write("Please select an option from the dropdown.")
