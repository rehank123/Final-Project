import streamlit as st

def print_welcome_message():
    st.write("# Welcome to Healthcare Chat Bot")
    st.write("## Information List")
    st.write("""
    1. About Medicine for Disease
    2. About Doctor for Disease
    3. About Hospital for Doctor
    """)

def get_user_input():
    return st.number_input("Please Enter a Number for the detail you want to know about:", min_value=1, max_value=3, step=1)

def handle_medicine_info():
    st.write("## List of diseases")
    diseases = {
        1: "Common Cold",
        2: "Influenza (Flu)",
        3: "Headache",
        4: "Allergies",
        5: "Bronchitis",
        6: "Pneumonia",
        7: "Stomach Flu (Gastroenteritis)",
        8: "Sinusitis",
        9: "Urinary Tract Infection (UTI)",
        10: "Conjunctivitis (Pink Eye)",
        11: "Sore Throat",
        12: "Ear Infection",
        13: "Fever",
        14: "Diabetes",
        15: "Hypertension",
        16: "Migraine",
        17: "Arthritis",
        18: "Asthma",
        19: "Acne",
        20: "Eczema"
    }
    disease = get_user_input()
    medicine = diseases.get(int(disease))
    if medicine:
        st.write(f"For {medicine}, take appropriate medicine.")
    else:
        st.write("Your disease is not in the list.")

def handle_doctor_info():
    st.write("## List of doctors")
    doctors = {
        1: "Dr. Saleem",
        2: "Dr. Abdullah",
        3: "Dr. Salman",
        4: "Dr. Kaleem",
        5: "Dr. Naimat",
        6: "Dr. Imran",
        7: "Dr. Kamran",
        8: "Dr. Moin",
        9: "Dr. Sultan",
        10: "Dr. Faizan",
        11: "Dr. Ali",
        12: "Dr. Aisha",
        13: "Dr. Omar",
        14: "Dr. Yasmin",
        15: "Dr. Ahmed",
        16: "Dr. Fatima",
        17: "Dr. Bilal",
        18: "Dr. Hina",
        19: "Dr. Usman",
        20: "Dr. Sarah"
    }
    doctor = get_user_input()
    doctor_name = doctors.get(int(doctor))
    if doctor_name:
        st.write(f"Your doctor is {doctor_name}.")
    else:
        st.write("Invalid Input.")

def handle_hospital_info():
    st.write("## List of Hospitals")
    hospitals = {
        1: "Muslim Care Hospital",
        2: "Islamic Health Center",
        3: "Al-Muslim Medical Center",
        4: "Nur Muslim Hospital",
        5: "Muslim Community Hospital",
        6: "Iman Muslim Hospital",
        7: "Muslim Welfare Hospital",
        8: "Safa Muslim Medical Center",
        9: "Muslim Relief Hospital",
        10: "Ummu Hospital",
        11: "Al-Hayat Hospital",
        12: "Noor Hospital",
        13: "Shifa Hospital",
        14: "Madina Hospital",
        15: "Niazi Hospital",
        16: "Gulshan Hospital",
        17: "Sughra Hospital",
        18: "Fatima Hospital",
        19: "City Hospital",
        20: "LifeCare Hospital"
    }
    hospital = get_user_input()
    hospital_name = hospitals.get(int(hospital))
    if hospital_name:
        st.write(f"Your hospital is {hospital_name}.")
    else:
        st.write("Invalid Input.")

def main():
    print_welcome_message()
    information = get_user_input()

    if information == 1:
        handle_medicine_info()
    elif information == 2:
        handle_doctor_info()
    elif information == 3:
        handle_hospital_info()
    else:
        st.write("Invalid Input. Please try again.")

if __name__ == "__main__":
    main()
