import streamlit as st

st.write("Welcome to Healthcare Chat Bot")

st.write("Information List")
choice = st.selectbox("Select an option", ["About Medicine for Disease", "About Doctor for Disease", "About Hospital for Doctor"])

if choice == "About Medicine for Disease":
    st.write("List of diseases")
    disease = st.selectbox("Select a disease", ["Common Cold", "Influenza (Flu)", "Headache", "Allergies", "Bronchitis", "Pneumonia", 
                                                "Stomach Flu (Gastroenteritis)", "Sinusitis", "Urinary Tract Infection (UTI)", 
                                                "Conjunctivitis (Pink Eye)"])
    if disease == "Common Cold":  
        st.write("Take Paracetamol")
    elif disease == "Influenza (Flu)":
        st.write("Take Tylenol")
    elif disease == "Headache":
        st.write("Take Ibuprofen")
    elif disease == "Allergies":
        st.write("Take Acetaminophen")
    elif disease == "Bronchitis":
        st.write("Take Aspirin")
    elif disease == "Pneumonia":
        st.write("Take Amoxicillin")
    elif disease == "Stomach Flu (Gastroenteritis)":
        st.write("Take Fexofenadine")
    elif disease == "Sinusitis":
        st.write("Take Ciprofloxacin")
    elif disease == "Urinary Tract Infection (UTI)":
        st.write("Take Zinc")
    elif disease == "Conjunctivitis (Pink Eye)":
        st.write("Take Diclofenac")
    else:
        st.write("Your disease is not in the list")

elif choice == "About Doctor for Disease":
    st.write("List of doctors")
    doctor = st.selectbox("Select a doctor", ["Dr. Saleem", "Dr. Abdullah", "Dr. Salman", "Dr. Kaleem", "Dr. Naimat", "Dr. Imran", 
                                              "Dr. Kamran", "Dr. Moin", "Dr. Sultan", "Dr. Faizan"])
    st.write("Your doctor is", doctor)

elif choice == "About Hospital for Doctor":
    st.write("List of Hospitals")
    hospital = st.selectbox("Select a hospital", ["Muslim Care Hospital", "Islamic Health Center", "Al-Muslim Medical Center", 
                                                  "Nur Muslim Hospital", "Muslim Community Hospital", "Iman Muslim Hospital", 
                                                  "Muslim Welfare Hospital", "Safa Muslim Medical Center", "Muslim Relief Hospital", 
                                                  "Ummu Hospital"])
    st.write("Your hospital is", hospital)

else:
    st.write("Invalid Input. Please try again.")
