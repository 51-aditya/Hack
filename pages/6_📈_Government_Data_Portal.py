import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Government data on different regions
data = {
    "Region": ["Region A", "Region B", "Region C", "Region D"],
    "Population": [100000, 150000, 200000, 120000],
    "Healthcare Spending": [2000000, 3000000, 2500000, 1800000],
    "Education Spending": [1500000, 1200000, 1800000, 1400000]
}

# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)

# Calculate per capita spending
df["Healthcare Per Capita"] = df["Healthcare Spending"] / df["Population"]
df["Education Per Capita"] = df["Education Spending"] / df["Population"]

# Streamlit app
def main():
    st.header("Government Data Analytics and Visualization")

    st.write(" ")

    st.subheader("Sample Data:")
    st.dataframe(df)

    st.write(" ")
    
    st.subheader("Per Capita Spending Visualization:")
    selected_metric = st.selectbox("Select Metric", ["Healthcare Per Capita", "Education Per Capita"])

    plt.figure(figsize=(8, 6))
    sns.barplot(x="Region", y=selected_metric, data=df)
    plt.title(f"{selected_metric} Across Regions")
    st.pyplot(plt)

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
