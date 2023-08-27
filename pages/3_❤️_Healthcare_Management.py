import streamlit as st
from datetime import datetime, timedelta
from faker import Faker
import random

fake = Faker()

# Generate fake doctor data
def generate_fake_doctor_data(num_doctors):
    doctor_data = []
    for _ in range(num_doctors):
        doctor = {
            "name": fake.name(),
            "specialization": fake.random_element(["Cardiologist", "Pediatrician", "Surgeon", "Dermatologist"]),
            "availability": {}
        }
        for _ in range(30):  # Simulate availability for 30 days
            date = (datetime.today() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
            doctor["availability"][date] = {
                "Morning": random.choice([True, False]),
                "Afternoon": random.choice([True, False]),
                "Evening": random.choice([True, False]),
                "Night": random.choice([True, False])
            }
        doctor_data.append(doctor)
    return doctor_data

# Sample data: Doctor availability
num_doctors = 10  # Number of doctors in the dataset
doctor_data = generate_fake_doctor_data(num_doctors)

def get_available_doctors(date, shift):
    available_doctors = []
    for doctor in doctor_data:
        if doctor["availability"].get(date, {}).get(shift, False):
            available_doctors.append(doctor)
    return available_doctors

def write_to_file(ps2, data):
    with open("ps2.txt", "a") as f:
        f.write(data + "\n")

def main():
    st.title("Healthcare Workforce Management")

    selected_date = st.date_input("Select a date", datetime.today())
    selected_shift = st.selectbox("Select a shift", ["Morning", "Afternoon", "Evening", "Night"])

    available_doctors = get_available_doctors(selected_date.strftime("%Y-%m-%d"), selected_shift)

    user_input_data = f"Selected Date: {selected_date.strftime('%Y-%m-%d')}, Selected Shift: {selected_shift}"
    write_to_file("ps2.txt", user_input_data)

    if available_doctors:
        doctor_list = "\n".join([f"{doctor['name']} - {doctor['specialization']}" for doctor in available_doctors])
        write_to_file("ps2.txt", "Available Doctors:\n" + doctor_list)
        write_to_file("ps2.txt", "\n")
    else:
        write_to_file("ps2.txt", "No doctors available for this shift.\n")

    st.subheader("Available doctors:")
    if available_doctors:
        for doctor in available_doctors:
            st.write(f"*{doctor['name']}*")
            st.write(f"Specialization: {doctor['specialization']}")
            st.write("---")
    else:
        st.write("No doctors available for this shift.")

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