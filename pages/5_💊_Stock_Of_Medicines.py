import streamlit as st

# Initialize Streamlit app
st.title("Medicine Stock Management")

# Initialize medicine stock dictionary
medicine_stock = {
    "Paxlovid": 10,
    "Molnupiravir": 10,
    "Remdesivir": 10,
    "Dexamethasone": 10,
    "Tocilizumab": 10,
}

# Function to distribute medicines
def distribute_medicines(selected_medicines):
    for medicine, quantity in selected_medicines.items():
        if medicine_stock[medicine] >= quantity:
            medicine_stock[medicine] -= quantity
            st.success(f"{quantity} {medicine} given to patient. Remaining stock: {medicine_stock[medicine]}")
        else:
            st.error(f"Insufficient stock for {medicine}. Cannot give {quantity}.")

# Display medicine options and quantities
st.subheader("Select Medicines and Quantities for Distribution")
selected_medicines = {}
for medicine in medicine_stock.keys():
    quantity = st.number_input(f"Quantity of {medicine}:", min_value=0, max_value=medicine_stock[medicine], value=0)
    selected_medicines[medicine] = quantity

if st.button("Give Medicines"):
    distribute_medicines(selected_medicines)

st.write(" ")

# Display medicine stocks
st.subheader("Medicine Stock Left")
for medicine, stock in medicine_stock.items():
    st.write(f"{medicine}: {stock}")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
