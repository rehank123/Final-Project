def print_welcome_message():
    print("Welcome to Healthcare Chat Bot ")
    print("Information List")
    print("""
    1. About Medicine for Disease
    2. About Doctor for Disease
    3. About Hospital for Doctor
    """)

def get_user_input():
    while True:
        try:
            return int(input("Please Enter a Number for the detail you want to know about: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            print()  # Add a blank line for better readability

def handle_medicine_info():
    print("List of diseases")
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
    medicine = diseases.get(disease)
    if medicine:
        print(f"For {medicine}, take appropriate medicine.")
    else:
        print("Your disease is not in the list.")

def handle_doctor_info():
    print("List of doctors")
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
    doctor_name = doctors.get(doctor)
    if doctor_name:
        print(f"Your doctor is {doctor_name}.")
    else:
        print("Invalid Input.")

def handle_hospital_info():
    print("List of Hospitals")
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
    hospital_name = hospitals.get(hospital)
    if hospital_name:
        print(f"Your hospital is {hospital_name}.")
    else:
        print("Invalid Input.")

def main():
    while True:
        print_welcome_message()
        information = get_user_input()

        if information == 1:
            handle_medicine_info()
            break
        elif information == 2:
            handle_doctor_info()
            break
        elif information == 3:
            handle_hospital_info()
            break
        else:
            print("Invalid Input. Please try again.")
            print()  # Add a blank line for better readability

if __name__ == "__main__":
    main()
