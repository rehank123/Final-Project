import streamlit as st

# Add title and introduction
st.title("Welcome to Healthcare Chat Bot")
st.write("Information List")
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
""")

# Add image
st.markdown(
    """
    <style>
    body {
        background-image: url("https://b2461891.smushcdn.com/2461891/wp-content/uploads/2022/09/cover.png?lossy=1&strip=1&webp=1");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
   

# Collect user input
information = st.text_input("Please Enter a Number for detail you want to know about:")

if information == "1":
  
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
  
  # Collect user input for disease
  disease = st.text_input("Enter the number of your disease:")

  if disease == "1":  
    st.write("Recommended medicine: Acetaminophen")
  elif disease == "2":
    st.write("Recommended medicine: Ibuprofen")
  elif disease == "3":
    st.write("Recommended medicine: Aspirin")
  elif disease == "4":
    st.write("Recommended medicine: Loratadine")
  elif disease == "5":
    st.write("Recommended medicine: Azithromycin")
  elif disease == "6":
    st.write("Recommended medicine: Amoxicillin")
  elif disease == "7":
    st.write("Recommended medicine: Loperamide")
  elif disease == "8":
    st.write("Recommended medicine: Decongestants")
  elif disease == "9":
    st.write("Recommended medicine: Phenazopyridine")
  elif disease == "10":
    st.write("Recommended medicine: Artificial tears")
  else:
    st.write("Your disease is not in the list")

elif information == "2":
  # Display list of diseases
  st.write("List of Diseases")
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
  
  # Collect user input for doctor
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
  # Display list of doctors
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
  
  # Collect user input for hospital
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
