import streamlit as st
import pandas as pd

# Define hospital data
hospital_data = {
    "Hospital A": {"Occupancy": 50, "Equipment": ["Patient Monitors", "ECG machine", "Sterilizers"]},
    "Hospital B": {"Occupancy": 30, "Equipment": ["Oxygen concentrator", "Patient Monitors", "ECG machine", "Sterilizers"]},
    "Hospital C": {"Occupancy": 80, "Equipment": ["X-Ray Machine", "ECG machine", "Ultrasound machine","Patient Monitors"]},
    "Hospital D": {"Occupancy": 20, "Equipment": ["X-ray Machine", "Defibrillator", "Ventilator"]},
    "Hospital E": {"Occupancy": 60, "Equipment": ["Ventilator", "Oxygen concentrator", "Ultrasound machine", "MRI Machine"]}
}

severity_data = {
    "Hospital A": {"Severity Level": (0,0.5)},
    "Hospital B": {"Severity Level": (0.5,1)},
    "Hospital C": {"Severity Level": (1,1.5)},
    "Hospital D": {"Severity Level": (1.5,2)},
    "Hospital E": {"Severity Level": (2,3)},
}
# Define symptom severity weights
symptom_weights = {
    "Fever": 0.6,
    "Cough": 0.4,
    "Reduced Oxygen levels": 0.9,
    "Fatigue": 0.5,
    "Body aches": 0.3,
    "Loss of taste or smell": 0.5,
    "Sore throat": 0.4,
    "Chest pain": 0.6
}

def write_to_file(ps1, data):
    with open("ps1.txt", "a") as f:
        f.write(data + "\n")

# Streamlit app
def main():
    st.header("Patient Hospital Allocation")

    # User input
    patient_name = st.text_input("Enter patient's name:")
    patient_age = st.number_input("Enter patient's age:", min_value=0, max_value=120, value=18)
    patient_gender = st.selectbox("Select patient's gender:", ["Male", "Female", "Other"])
    sickness_duration = st.number_input("Enter duration of sickness in days:", min_value=1)


    st.write(" ")

    selected_symptoms = st.multiselect(
        "Select Symptopms:",
        list(symptom_weights.keys())
    )

    # Calculate severity
    total_symptom_weight = sum(symptom_weights[symptom] for symptom in selected_symptoms)
    severity_level = total_symptom_weight * (sickness_duration / 10)

    st.markdown(f"#### Severity Level: {severity_level:.2f}")

    # Allocate hospital based on severity range
    allocated_hospital = None
    for severity, data in severity_data.items():
        if data["Severity Level"][0] <= severity_level < data["Severity Level"][1]:
            allocated_hospital = severity
            break

    if len(allocated_hospital)>0:
        st.success(f"Based on your severity score, you have been allocated {allocated_hospital}.")
        st.markdown("### Hospital Details")
        st.table(pd.DataFrame([hospital_data[allocated_hospital]], columns=["Occupancy", "Equipment"]))
        accept_hospital = st.button("Accept Allocated Hospital")
        if accept_hospital:
            hospital_data[allocated_hospital]["Occupancy"] -= 1
            st.success(f"You have accepted the allocation.")
            st.markdown("### Updated Hospital Occupancy")
            st.table(pd.DataFrame(hospital_data.values(), index=hospital_data.keys()))

            # Call write_to_file function to store user input data
            user_input_data = f"Name: {patient_name}, Age: {patient_age}, Gender: {patient_gender}, Duration: {sickness_duration} days, Symptoms: {', '.join(selected_symptoms)}, Severity Level: {severity_level:.2f}, Allocated Hospital: {allocated_hospital if allocated_hospital else 'Not allocated'}"
            write_to_file("ps1.txt", user_input_data)
    else:
        st.error("No suitable hospital found for your severity score.")

if __name__ == "__main__":
    main()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)