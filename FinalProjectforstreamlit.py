import streamlit as st

st.title("Welcome to Healthcare Chat Bot ")

st.write("Information List")
st.write("""
1. Find Medicines for Diseases
2. Find Doctors for Specific Diseases
3. Locate Hospitals with Specialized Doctors
""")

information = st.text_input("Please Enter a Number for detail you want to know about:")

if information == "1":
    st.write("List of disease")
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

    disease = st.text_input("Enter the number of your disease you want medicine for it:")

    if disease == "1":
        st.write("Recommended Medicine: Paracetamol")
    elif disease == "2":
        st.write("Recommended Medicine: Tylenol")
    elif disease == "3":
        st.write("Recommended Medicine: Ibuprofen")
    elif disease == "4":
        st.write("Recommended Medicine: Acetaminophen")
    elif disease == "5":
        st.write("Recommended Medicine: Aspirin")
    elif disease == "6":
        st.write("Recommended Medicine: Amoxicillin")
    elif disease == "7":
        st.write("Recommended Medicine: Fexofenadine")
    elif disease == "8":
        st.write("Recommended Medicine: Ciprofloxacin")
    elif disease == "9":
        st.write("Recommended Medicine: Zinc")
    elif disease == "10":
        st.write("Recommended Medicine: Diclofenac")
    else:
        st.write("Your disease is not in the list")

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
    doctor = st.text_input("Enter the number of your Doctor you want to know about it:")

    if doctor == "1":
        st.write("Recommended Doctor: Dr. Saleem")
    elif doctor == "2":
        st.write("Recommended Doctor: Dr. Abdullah")
    elif doctor == "3":
        st.write("Recommended Doctor: Dr. Salman")
    elif doctor == "4":
        st.write("Recommended Doctor: Dr. Kaleem")
    elif doctor == "5":
        st.write("Recommended Doctor: Dr. Naimat")
    elif doctor == "6":
        st.write("Recommended Doctor: Dr. Imran")
    elif doctor == "7":
        st.write("Recommended Doctor: Dr. Kamran")
    elif doctor == "8":
        st.write("Recommended Doctor: Dr. Moin")
    elif doctor == "9":
        st.write("Recommended Doctor: Dr. Sultan")
    elif doctor == "10":
        st.write("Recommended Doctor: Dr. Faizan")
    else:
        st.write("Invalid Input")

elif information == "3":
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
    hospital = st.text_input("Enter the number of your Hospital:")

    if hospital == "1":
        st.write("Muslim Care Hospital")
    elif hospital == "2":
        st.write("Islamic Health Center")
    elif hospital == "3":
        st.write("Al-Muslim Medical Center")
    elif hospital == "4":
        st.write("Nur Muslim Hospital")
    elif hospital == "5":
        st.write("Muslim Community Hospital")
    elif hospital == "6":
        st.write("Iman Muslim Hospital")
    elif hospital == "7":
        st.write("Muslim Welfare Hospital")
    elif hospital == "8":
        st.write("Safa Muslim Medical Center")
    elif hospital == "9":
        st.write("Muslim Relief Hospital")
    elif hospital == "10":
        st.write("Ummu Hospital")

else:
    st.write("Invalid Input")
