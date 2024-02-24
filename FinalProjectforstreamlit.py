import streamlit as st

st.write("Welcome to Healthcare Chat Bot")

st.write("Information List")
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
""")

information = st.number_input("Please Enter a Number for the detail you want to know about:", min_value=1, max_value=3, step=1)

if information == 1:
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
    disease = st.number_input("Enter the number of your disease:", min_value=1, max_value=10, step=1)
    if disease == 1:
        st.write("Take Paracetamol")
    elif disease == 2:
        st.write("Take Tylenol")
    elif disease == 3:
        st.write("Take Ibuprofen")
    # Add more conditions for other diseases
    else:
        st.write("Your disease is not in the list.")

elif information == 2:
    st.write("List of doctors")
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
    doctor = st.number_input("Enter the number of your doctor:", min_value=1, max_value=10, step=1)
    if doctor == 1:
        st.write("Your doctor is Dr. Saleem.")
    elif doctor == 2:
        st.write("Your doctor is Dr. Abdullah.")
    # Add more conditions for other doctors
    else:
        st.write("Invalid Input.")

elif information == 3:
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
    hospital = st.number_input("Enter the number of your hospital:", min_value=1, max_value=10, step=1)
    if hospital == 1:
        st.write("Your hospital is Muslim Care Hospital.")
    elif hospital == 2:
        st.write("Your hospital is Islamic Health Center.")
    # Add more conditions for other hospitals
    else:
        st.write("Invalid Input.")

else:
    st.write("Invalid Input. Please try again.")
