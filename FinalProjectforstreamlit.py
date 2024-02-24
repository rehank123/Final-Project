import streamlit as st






# Add a title
st.title('Animated Streamlit Example')

# Write some text
st.write("Here's a simple animation using HTML and CSS:")

# Write HTML with CSS animation
st.write("""
<div style="width: 100px; height: 100px; background-color: red;
            position: relative; animation-name: example; 
            animation-duration: 4s; animation-iteration-count: infinite;">
</div>

<style>
@keyframes example {
  0%   {background-color:red; left:0px; top:0px;}
  25%  {background-color:yellow; left:200px; top:0px;}
  50%  {background-color:blue; left:200px; top:200px;}
  75%  {background-color:green; left:0px; top:200px;}
  100% {background-color:red; left:0px; top:0px;}
}
</style>
""")

















st.title("Welcome to Healthcare Chatbot")
st.write("Information List")
st.write("""
1. About Medicine for Disease
2. About Doctor for Disease
3. About Hospital for Doctor
""")

information = st.text_input("Please Enter a Number for detail you want to know about:")

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
  
  disease = st.text_input("Enter the number of your disease for Medicine:")

  if disease == "1":  
    st.write("Recommended medicine: Acetaminophen")
  elif disease == "2":
    st.write("Recommended medicine: Ibuprofen")
  elif disease == "3":
    st.write("Recommended medicine: Aspirin")
  elif disease == "4":
    st.write("Recommended medicine: Loratadine")
  elif disease == "5":
    st.write("Recommended medicine: Paclitaxel")
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
  st.write("List of Diseases")
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
  doctor = st.text_input("Enter the number of your Doctor for Diseases:")

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
  doctor = st.text_input("Enter the number of your Doctor for Hospital:")

  if doctor == "1":
    st.write("Hospital Name: Zia Care Hospital")
  elif doctor == "2":
    st.write("Hospital Name: Noor Health Center")
  elif doctor == "3":
    st.write("Hospital Name: Al-Muslim Medical Center")
  elif doctor == "4":
    st.write("Hospital Name: Sultan Hospital")
  elif doctor == "5":
    st.write("Hospital Name: Shaukat Khanum")
  elif doctor == "6":
    st.write("Hospital Name: Imam Clinic Hospital")
  elif doctor == "7":
    st.write("Hospital Name: Muslim Welfare Hospital")
  elif doctor == "8":
    st.write("Hospital Name: Safa  Medical Center")
  elif doctor == "9":
    st.write("Hospital Name: Al Khidmat Hospital")
  elif doctor == "10":
    st.write("Hospital Name: Zain Hospital")

else:
  st.write("Invalid Input")
