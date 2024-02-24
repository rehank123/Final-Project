import streamlit as st

def main():
    st.title("Welcome to Healthcare Chat Bot")
    
    while True:
        st.write("Information List")
        st.write("""
        1. About Medicine for Disease
        2. About Doctor for Disease
        3. About Hospital for Doctor
        """)
        
        information = st.text_area("Please Enter a Number for detail you want to know about:")
        
        if information == "1":
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
            doctor = st.text_area("Enter the number of your Doctor:")
            
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
            10.Dr. Faizan
            """)
            doctor = st.text_area("Enter the number of your Doctor:")
            
            if doctor == "1":
                st.write("Muslim Care Hospital")
            elif doctor == "2":
                st.write("Islamic Health Center")
            elif doctor == "3":
                st.write("Al-Muslim Medical Center")
            elif doctor == "4":
                st.write("Nur Muslim Hospital")
            elif doctor == "5":
                st.write("Muslim Community Hospital")
            elif doctor == "6":
                st.write("Iman Muslim Hospital")
            elif doctor == "7":
                st.write("Muslim Welfare Hospital")
            elif doctor == "8":
                st.write("Safa Muslim Medical Center")
            elif doctor == "9":
                st.write("Muslim Relief Hospital")
            elif doctor == "10":
                st.write("Ummu Hospital")
        else:
            st.write("Invalid Input")
            
        repeat = st.radio("Do you want to inquire about another topic?", ("Yes", "No"))
        if repeat == "No":
            break

if __name__
