import streamlit as st

def main():
    st.title("Healthcare Chat Bot")

    information = st.sidebar.selectbox("Information List", ["About Medicine for Disease", "About Doctor for Disease", "About Hospital for Doctor"])

    if information == "About Medicine for Disease":
        st.subheader("List of Diseases")
        diseases = [
            "Common Cold", "Influenza (Flu)", "Headache", "Allergies", "Bronchitis",
            "Pneumonia", "Stomach Flu (Gastroenteritis)", "Sinusitis", "Urinary Tract Infection (UTI)",
            "Conjunctivitis (Pink Eye)"
        ]
        disease = st.selectbox("Select Disease", diseases)
        if disease:
            st.write(f"For {disease}, take appropriate medicine.")

    elif information == "About Doctor for Disease":
        st.subheader("List of Doctors")
        doctors = [
            "Dr. Saleem", "Dr. Abdullah", "Dr. Salman", "Dr. Kaleem", "Dr. Naimat",
            "Dr. Imran", "Dr. Kamran", "Dr. Moin", "Dr. Sultan", "Dr. Faizan"
        ]
        doctor = st.selectbox("Select Doctor", doctors)
        if doctor:
            st.write(f"Your doctor is {doctor}.")

    elif information == "About Hospital for Doctor":
        st.subheader("List of Hospitals")
        hospitals = [
            "Muslim Care Hospital", "Islamic Health Center", "Al-Muslim Medical Center",
            "Nur Muslim Hospital", "Muslim Community Hospital", "Iman Muslim Hospital",
            "Muslim Welfare Hospital", "Safa Muslim Medical Center", "Muslim Relief Hospital",
            "Ummu Hospital"
        ]
        hospital = st.selectbox("Select Hospital", hospitals)
        if hospital:
            st.write(f"Your hospital is {hospital}.")

if __name__ == "__main__":
    main()
