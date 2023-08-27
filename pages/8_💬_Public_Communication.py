import streamlit as st

# Sample data: Healthcare facility availability
facility_data = [
    {"Facility": "Hospital A", "Available Beds": 20, "Available Ventilators": 5},
    {"Facility": "Hospital B", "Available Beds": 15, "Available Ventilators": 2},
    {"Facility": "Clinic X", "Available Beds": 8, "Available Ventilators": 0},
]

# Sample data: Testing centers
testing_centers = [
    {"Center": "Testing Center 1", "Location": "City A"},
    {"Center": "Testing Center 2", "Location": "City B"},
    {"Center": "Testing Center 3", "Location": "City C"},
]

# Streamlit app
def main():
    st.title("Public Health Information")

    st.write(" ")

    # Display healthcare facility availability
    st.subheader("Healthcare Facility Availability")
    st.table(facility_data)

    # Display testing centers
    st.subheader("Testing Centers")
    st.table(testing_centers)

    # Display safety guidelines
    st.subheader("Safety Guidelines")
    st.markdown("""
    - Practice good hand hygiene by washing hands frequently.
    - Wear a mask in public places to reduce the risk of transmission.
    - Maintain physical distancing of at least 1 meter from others.
    - Stay home if you are feeling unwell or experiencing symptoms.
    - Follow local health authority guidelines for self-isolation and quarantine.
    """)

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
