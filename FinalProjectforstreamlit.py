import streamlit as st

st.write("Welcome to Healthcare Chat Bot ")

st.write("Information List")
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
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

    disease = st.text_input("Enter the number of your disease:")

    if disease == "1":
        st.write("Take Paracetamol")
    elif disease == "2":
        st.write("Take Tylenol")
    elif disease == "3":
        st.write("Take Ibuprofen")
    elif disease == "4":
        st.write("Take Acetaminophen")
    elif disease == "5":
        st.write("Take Aspirin")
    elif disease == "6":
        st.write("Take Amoxicillin")
    elif disease == "7":
        st.write("Take Fexofenadine")
    elif disease == "8":
        st.write("Take Ciprofloxacin")
    elif disease == "9":
        st.write("Take Zinc")
    elif disease == "10":
        st.write("Take Diclofenac")
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
    doctor = st.text_input("Enter the number of your Doctor:")

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
