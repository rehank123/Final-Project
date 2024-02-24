import streamlit as st

st.title("Welcome to Healthcare Chatbot")

# Display a welcome message
st.write("Welcome to the Healthcare Chatbot! Please select an option from the list below:")

# Display the information list
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
""")

# Get user input
information = st.text_input("Please enter a number for the detail you want to know about:")

# Function to display recommended medicine
def display_medicine(disease):
    medicines = {
        "1": "Acetaminophen",
        "2": "Ibuprofen",
        "3": "Aspirin",
        "4": "Loratadine",
        "5": "Paclitaxel",
        "6": "Amoxicillin",
        "7": "Loperamide",
        "8": "Decongestants",
        "9": "Phenazopyridine",
        "10": "Artificial tears"
    }
    return medicines.get(disease, "Unknown")

# Function to display doctor
def display_doctor(doctor):
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

# Function to display hospital
def display_hospital(hospital):
    hospitals = {
        "1": "Zia Care Hospital",
        "2": "Noor Health Center",
        "3": "Al-Muslim Medical Center",
        "4": "Sultan Hospital",
        "5": "Shaukat Khanum",
        "6": "Imam Clinic Hospital",
        "7": "Muslim Welfare Hospital",
        "8": "Safa Medical Center",
        "9": "Al Khidmat Hospital",
        "10": "Zain Hospital"
    }
    return hospitals.get(hospital, "Unknown")

# Display information based on user input
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
    disease = st.text_input("Enter the number of your disease:")
    st.write("Recommended medicine:", display_medicine(disease))

elif information == "2":
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
    doctor = st.text_input("Enter the number of your Doctor:")
    st.write("Selected Doctor:", display_doctor(doctor))

elif information == "3":
    st.write("List of Hospitals")
    st.write("""
    1. Zia Care Hospital
    2. Noor Health Center
    3. Al-Muslim Medical Center
    4. Sultan Hospital
    5. Shaukat Khanum
    6. Imam Clinic Hospital
    7. Muslim Welfare Hospital
    8. Safa Medical Center
    9. Al Khidmat Hospital
    10. Zain Hospital
    """)
    hospital = st.text_input("Enter the number of your Hospital:")
    st.write("Selected Hospital:", display_hospital(hospital))

else:
    st.write("Invalid Input")
